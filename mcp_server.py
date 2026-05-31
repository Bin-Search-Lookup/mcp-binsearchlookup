"""
BinSearchLookup Enterprise MCP Server
=====================================
A production-grade Model Context Protocol (MCP) server for BinSearchLookup.

Features:
- Offline Local Diagnostics: Luhn checks & Network identification
- Auto-chunking & Concurrency for batch lookups > 50 BINs
- In-memory LRU caching to reduce API costs
- Strict input sanitization
- Resiliency with exponential backoff
"""

import os
import sys
import json
import logging
import asyncio
import re
from typing import List, Dict, Any

import httpx
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from mcp.server.fastmcp import FastMCP
from cachetools import TTLCache

# Load environment variables
load_dotenv()

# Sanitized logging to stderr to preserve MCP JSON-RPC protocol on stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stderr)]
)
logger = logging.getLogger("bsl-mcp")

# Initialize FastMCP server
mcp = FastMCP("BinSearchLookup")
BASE_URL = "https://api.binsearchlookup.com"

# Caching: Store up to 1000 items for 1 hour (3600 seconds)
cache = TTLCache(maxsize=1000, ttl=3600)

# Concurrency limits: Prevent slamming the API for huge batch requests
MAX_CONCURRENT_REQUESTS = 3
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

# --- Authentication & Resiliency ---

class RateLimitError(Exception):
    pass

def get_headers() -> dict:
    api_key = os.environ.get("BSL_API_KEY")
    user_id = os.environ.get("BSL_USER_ID")
    
    if not api_key or not user_id:
        logger.error("Missing BSL_API_KEY or BSL_USER_ID environment variables.")
        raise ValueError("Authentication failed: 'BSL_API_KEY' and 'BSL_USER_ID' environment variables must be set.")
        
    return {
        "X-API-Key": api_key,
        "X-User-ID": user_id,
        "Content-Type": "application/json"
    }

@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=(retry_if_exception_type((httpx.RequestError, RateLimitError))),
    before_sleep=lambda retry_state: logger.warning(f"Retrying request... Attempt {retry_state.attempt_number}")
)
async def make_api_request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    url = f"{BASE_URL}{endpoint}"
    # Use headers without overriding custom ones entirely
    headers = get_headers() if not endpoint.startswith("/health") else {}
    
    if "headers" in kwargs:
        kwargs["headers"].update(headers)
    else:
        kwargs["headers"] = headers

    kwargs.setdefault("timeout", 15.0)

    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, **kwargs)
        if response.status_code == 429:
            logger.warning("Rate limit exceeded (429). Triggering retry.")
            raise RateLimitError("Rate limit exceeded.")
        response.raise_for_status()
        return response.json()

# --- Offline Diagnostics (Luhn & Networks) ---

def sanitize_bin(v: str) -> str:
    """Removes all non-digit characters from the BIN/PAN."""
    cleaned = re.sub(r'\D', '', v)
    if not cleaned:
        raise ValueError("Input must contain digits.")
    return cleaned

def check_luhn(card_number: str) -> bool:
    """Perform Luhn algorithm validation on a string of digits."""
    if not card_number.isdigit(): 
        return False
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9: 
                n -= 9
        total += n
    return total % 10 == 0

def identify_network(number: str) -> str:
    """Identify card network based on standard global prefixes."""
    if not number: return "Unknown"
    
    # Amex
    if number.startswith(('34', '37')): return "American Express"
    # Diners Club
    if number.startswith(('36', '38', '39')) or (len(number) >= 3 and 300 <= int(number[:3]) <= 305): 
        return "Diners Club International"
    # JCB
    if len(number) >= 4 and 3528 <= int(number[:4]) <= 3589: return "JCB"
    # Visa & Elo overlapping
    if number.startswith('4'): 
        if number.startswith(('4011', '4312', '4389', '4514', '4576')): return "Elo"
        return "Visa"
    # Mastercard
    if len(number) >= 4 and 2221 <= int(number[:4]) <= 2720: return "Mastercard"
    if number.startswith(('51', '52', '53', '54', '55')): return "Mastercard"
    # Troy
    if number.startswith('9792'): return "Troy"
    # Dankort
    if number.startswith('5019'): return "Dankort"
    # MIR
    if len(number) >= 4 and 2200 <= int(number[:4]) <= 2204: return "MIR"
    # Discover
    if number.startswith('6011') or number.startswith(('644', '645', '646', '647', '648', '649', '65')) or (len(number) >= 6 and 622126 <= int(number[:6]) <= 622925): 
        return "Discover"
    # UnionPay
    if number.startswith('62'):
        if number.startswith('6277'): return "Elo"
        return "UnionPay"
    # Elo specific
    if number.startswith(('5041', '5066', '5090', '6362', '6363')): return "Elo"
    # RuPay
    if number.startswith(('60', '65', '81', '82', '508')): return "RuPay (or Discover/Maestro)"
    # Maestro
    if number.startswith('50') or (len(number) >= 2 and 56 <= int(number[:2]) <= 69): 
        return "Maestro (or Regional)"
    
    return "Unknown / Co-branded / Local Network"

# --- Pydantic Schemas ---

class LookupRequest(BaseModel):
    bin_number: str = Field(..., description="The 6-8 digit Bank Identification Number (BIN) to lookup.")

    @field_validator("bin_number")
    @classmethod
    def clean_bin(cls, v: str) -> str:
        clean = sanitize_bin(v)
        if len(clean) >= 13 and not check_luhn(clean):
            raise ValueError("Input appears to be a full card number but failed the Luhn check. Request blocked locally to save API quota.")
        return clean[:8] if len(clean) >= 8 else clean

class BatchLookupRequest(BaseModel):
    bins: List[str] = Field(..., description="A list of BINs to lookup. Can be any size; the server will auto-chunk.")

    @field_validator("bins")
    @classmethod
    def clean_bins(cls, v: List[str]) -> List[str]:
        cleaned_bins = []
        for b in v:
            try:
                c = sanitize_bin(b)
                if len(c) >= 13 and not check_luhn(c):
                    # Skip invalid full PANs to save quota
                    logger.warning(f"Batch item skipped: Full card number failed Luhn check.")
                    continue
                cleaned_bins.append(c[:8] if len(c) >= 8 else c)
            except ValueError:
                continue
        if not cleaned_bins:
            raise ValueError("No valid BINs provided in the batch.")
        return cleaned_bins

class QuotaRequest(BaseModel):
    public_user_id: str = Field(..., description="Your public user ID (UUID format).")

# --- MCP Tools ---

@mcp.tool()
async def local_card_diagnostics(number: str) -> str:
    """
    Perform FREE, local, offline diagnostics on a BIN or full PAN (Primary Account Number).
    Identifies the Card Network (Visa, Amex, etc.) and performs Luhn validation for 16-digit cards.
    Use this BEFORE the online lookup API if the user provides a full card number, 
    to protect PCI data and avoid sending full PANs over the network.
    """
    try:
        clean_num = sanitize_bin(number)
        network = identify_network(clean_num)
        
        result = {
            "input_length": len(clean_num),
            "identified_network": network,
            "offline_check": True
        }
        
        if len(clean_num) >= 13:
            result["luhn_valid"] = check_luhn(clean_num)
            result["is_full_pan"] = True
            result["security_warning"] = "Full PAN detected. To protect sensitive data, do not send the full number to the BIN lookup API. Only send the 'recommended_bin'."
            result["recommended_bin"] = clean_num[:8]
        else:
            result["is_full_pan"] = False
            result["luhn_valid"] = "N/A (Number too short for reliable Luhn check)"
            
        return json.dumps(result, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})

@mcp.tool()
async def lookup_bin(bin_number: str) -> str:
    """
    Retrieves detailed information for a single Bank Identification Number (BIN) via API.
    Automatically strips spaces, drops extra digits to 8 max, and caches results.
    """
    try:
        req = LookupRequest(bin_number=bin_number)
        clean_bin = req.bin_number
        
        cache_key = f"bin_{clean_bin}"
        if cache_key in cache:
            logger.info(f"Cache hit for BIN: {clean_bin}")
            return json.dumps(cache[cache_key], indent=2)

        logger.info(f"Looking up BIN: {clean_bin}")
        data = await make_api_request("GET", "/lookup", params={"bin": clean_bin})
        
        if data.get("success"):
            cache[cache_key] = data
            
        return json.dumps(data, indent=2)
    except Exception as e:
        logger.error(f"Lookup failed for BIN {bin_number}: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
async def batch_lookup_bins(bins: List[str]) -> str:
    """
    Processes multiple BIN lookups via API in a single request. 
    Accepts unlimited BINs by automatically chunking into groups of 50.
    """
    try:
        req = BatchLookupRequest(bins=bins)
        clean_bins = list(set(req.bins)) # deduplicate
        
        results = {"success": True, "data": [], "errors": []}
        bins_to_fetch = []

        for b in clean_bins:
            cache_key = f"bin_{b}"
            if cache_key in cache:
                results["data"].append(cache[cache_key]["data"])
            else:
                bins_to_fetch.append(b)

        if not bins_to_fetch:
            logger.info("All BINs served from cache!")
            return json.dumps(results, indent=2)

        chunks = [bins_to_fetch[i:i + 50] for i in range(0, len(bins_to_fetch), 50)]
        logger.info(f"Fetching {len(bins_to_fetch)} BINs in {len(chunks)} chunks.")

        async def fetch_chunk(chunk: List[str]):
            async with semaphore:
                return await make_api_request("POST", "/lookup/batch", json={"bins": chunk})

        tasks = [fetch_chunk(chunk) for chunk in chunks]
        chunk_responses = await asyncio.gather(*tasks, return_exceptions=True)

        for i, response in enumerate(chunk_responses):
            if isinstance(response, Exception):
                logger.error(f"Chunk {i} failed: {response}")
                results["errors"].append({"chunk": chunks[i], "error": str(response)})
                results["success"] = False
            else:
                if response.get("success") and "data" in response:
                    for item in response["data"]:
                        if "BIN" in item:
                            cache[f"bin_{item['BIN']}"] = {"success": True, "data": item, "statusCode": 200}
                        results["data"].append(item)
                else:
                    results["errors"].append({"chunk": chunks[i], "error": "API returned failure for chunk"})

        return json.dumps(results, indent=2)

    except Exception as e:
        logger.error(f"Batch lookup failed: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
async def check_quota(public_user_id: str) -> str:
    """Checks current API usage and limits for the provided user ID."""
    try:
        logger.info(f"Checking quota for user: {public_user_id}")
        data = await make_api_request("GET", f"/api/quota/{public_user_id}")
        return json.dumps(data, indent=2)
    except Exception as e:
        logger.error(f"Quota check failed: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
async def check_system_health() -> str:
    """Diagnostic tool to check if the API is currently online."""
    try:
        logger.info("Checking API system health...")
        health_data = await make_api_request("GET", "/health")
        return json.dumps({"health": health_data}, indent=2)
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return json.dumps({"error": f"API appears to be offline or unreachable: {str(e)}"})

# --- MCP Resources & Prompts ---

@mcp.resource("mcp://binsearchlookup/docs/errors")
def get_error_docs() -> str:
    return '''
    BinSearchLookup API Error Codes:
    - 400 MISSING_BIN_PARAMETER: The `bin` parameter was not provided.
    - 400 INVALID_BIN: The provided BIN format is incorrect.
    - 401 UNAUTHORIZED: Missing or invalid X-API-Key or X-User-ID headers. Check environment variables.
    - 403 ACCESS_DENIED: The API key does not have permission for this endpoint.
    - 403 NO_SUBSCRIPTION: The user does not have an active subscription.
    - 429 RATE_LIMIT_EXCEEDED: Too many requests. Server auto-retries, but may fail if sustained.
    - 500 INTERNAL_ERROR: BinSearchLookup server experienced an issue.
    '''

@mcp.resource("mcp://binsearchlookup/docs/api")
def get_api_docs() -> str:
    return '''
    BinSearchLookup API Structure:
    - Base URL: https://api.binsearchlookup.com
    - Successful responses contain: `{"success": true, "data": {...}, "statusCode": 200}`
    - The `data` object contains: `BIN`, `Brand`, `Type`, `Issuer`, `CountryName`, `Category`.
    '''

@mcp.prompt()
def fraud_analysis(number: str) -> str:
    """Analyze a specific BIN or full Card Number for fraud indicators."""
    return f'''
    Please analyze the number {number} for potential risk and fraud indicators.
    
    Steps to follow:
    1. FIRST, run the `local_card_diagnostics` tool on {number} to identify the network and check the Luhn validity (especially if it is a full 16-digit card).
    2. If the user provided a full card number, extract ONLY the recommended 6-8 digit BIN from the diagnostic output to protect their privacy.
    3. Use the `lookup_bin` tool to fetch the detailed BIN data for the 6-8 digit BIN.
    4. Provide a structured risk assessment report focusing on:
       - Is the card number mathematically valid?
       - Card Brand & Type (e.g., Credit vs. Debit vs. Prepaid risk levels).
       - Issuer Bank and Country (Are there geographical risks?).
    5. If you encounter any API errors, call `check_system_health` or consult `mcp://binsearchlookup/docs/errors`.
    '''

@mcp.prompt()
def bulk_bin_audit(bins_comma_separated: str) -> str:
    """Perform a bulk audit on a comma-separated list of BINs."""
    return f'''
    I need a bulk audit report for the following BINs: {bins_comma_separated}
    
    Steps to follow:
    1. Parse the comma-separated string into a list of BINs.
    2. Use the `batch_lookup_bins` tool to fetch data for all of them at once. (It handles chunking and limits automatically).
    3. Format the results into a markdown table.
    4. Highlight any BINs that are "Prepaid" or from high-risk countries.
    '''

if __name__ == "__main__":
    logger.info("Starting BinSearchLookup Enterprise MCP Server...")
    mcp.run(transport='stdio')
