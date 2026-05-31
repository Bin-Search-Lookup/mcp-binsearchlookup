# BinSearchLookup MCP Server

**Select Language:**
[English](README.md) | [Français](docs/README-fr.md) | [Español](docs/README-es.md) | [Deutsch](docs/README-de.md) | [Italiano](docs/README-it.md) | [Português](docs/README-pt.md) | [Русский](docs/README-ru.md) | [中文](docs/README-zh.md) | [日本語](docs/README-ja.md) | [한국어](docs/README-ko.md) | [العربية](docs/README-ar.md)

---

The official Model Context Protocol (MCP) server for [BinSearchLookup.com](https://www.binsearchlookup.com/).

This server allows AI agents (like Claude Desktop, Cursor, and custom LLMs) to seamlessly and securely interface with the BinSearchLookup API to perform advanced Bank Identification Number (BIN) lookups, fraud analysis, and bulk card auditing.

## Enterprise Features

- **Local Offline Diagnostics & Pre-Flight Checks:** Identifies networks (Visa, Mastercard, Amex, etc.) and performs offline Luhn algorithm checks on full 16-digit PANs locally. Invalid numbers are blocked before hitting the API, protecting your quota and keeping full PANs secure.
- **Auto-Chunking & Concurrency:** Submit thousands of BINs at once. The server automatically de-duplicates, chunks them into batches of 50, and processes them concurrently while respecting rate limits.
- **In-Memory LRU Caching:** Duplicate AI requests within the same session are served instantly from memory, saving your API credits.
- **Strict Input Sanitization:** Automatically strips dashes, letters, and whitespace from LLM inputs.
- **Resiliency:** Built-in exponential backoff using `tenacity` handles network blips and `429 Rate Limit` errors gracefully.
- **Zero-Install Deployment:** Run entirely inside a lightweight Docker container.

## Installation & Usage

You can run this MCP server in two ways: using Docker (Recommended) or locally via Python.

### Option 1: Docker (Recommended - Zero Install)

If you are using Claude Desktop or an MCP-compatible client that supports Docker, simply add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "BSL_API_KEY=bsl_your_api_key_here",
        "-e", "BSL_USER_ID=your_user_id_here",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```
*(Alternatively, build the provided `Dockerfile` and run your own local image).*

### Option 2: Local Python

1. **Install requirements:**
   ```bash
   pip install httpx pydantic tenacity python-dotenv mcp cachetools
   ```
2. **Configure your `.env` file:**
   Create a `.env` file in the same directory as `mcp_server.py`:
   ```env
   BSL_API_KEY=bsl_your_api_key_here
   BSL_USER_ID=your_uuid_here
   ```
3. **Add to your MCP Client Configuration:**
   ```json
   {
     "mcpServers": {
       "binsearchlookup": {
         "command": "python3",
         "args": ["/absolute/path/to/mcp_server.py"]
       }
     }
   }
   ```

## Available MCP Tools

- `local_card_diagnostics(number: str)`: FREE, offline tool to identify networks and perform Luhn validation.
- `lookup_bin(bin_number: str)`: Retrieves detailed information for a single BIN.
- `batch_lookup_bins(bins: List[str])`: Processes multiple BIN lookups at once (handles unlimited BINs via chunking).
- `check_quota(public_user_id: str)`: Checks current API usage and limits.
- `check_system_health()`: Diagnostic tool to check API uptime status.

## Pre-Configured AI Prompts

The server exposes built-in prompts to help your AI execute complex tasks instantly:
- **`fraud_analysis`**: Instructs the LLM to run offline diagnostics first, extract the secure BIN, fetch API data, and generate a comprehensive risk assessment.
- **`bulk_bin_audit`**: Instructs the LLM to take a comma-separated list of BINs, process them in bulk, and generate a markdown table highlighting prepaid or high-risk origin countries.

## Pricing & Limits

BinSearchLookup offers flexible tiers depending on your API needs. The MCP server automatically handles these limits via exponential backoff if exceeded.

| Plan | Price (Monthly / Yearly) | Rate Limit | Monthly Quota | API Keys |
|---|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 requests / month | 1 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 requests / month | 3 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 requests / month | 15 |
| **Enterprise** | $999 / $980 | 768 req/min | Unlimited requests | 190 |

*Upgrade your plan at [BinSearchLookup Dashboard](https://www.binsearchlookup.com/dashboard).*

---
*Built for the Model Context Protocol.*
