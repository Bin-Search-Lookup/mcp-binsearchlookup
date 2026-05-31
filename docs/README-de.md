**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# BinSearchLookup MCP Server

Der offizielle Model Context Protocol (MCP) Server für [BinSearchLookup.com](https://www.binsearchlookup.com/).

Ermöglicht KI-Agenten die sichere Interaktion mit der API für BIN-Lookups, Betrugsanalysen und Massen-Audits.

## Enterprise-Funktionen

- **Lokale Offline-Diagnose & Pre-Flight Checks:** Identifiziert Netzwerke und validiert den Luhn-Algorithmus lokal.
- **Automatisches Chunking & Concurrency:** Senden Sie Tausende von BINs gleichzeitig.
- **In-Memory LRU Caching:** Doppelte Anfragen werden sofort aus dem Speicher beantwortet.
- **Strenge Eingabebereinigung:** Bereinigt automatisch unsaubere Eingaben.
- **Resilienz:** Integrierter exponentieller Backoff.
- **Zero-Install Deployment:** Vollständig über Docker ausführbar.

## Installation & Nutzung

### Option 1: Docker (Empfohlen)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_dein_api_key",
        "-e", "BSL_USER_ID=deine_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### Option 2: Lokales Python
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. Erstellen Sie eine `.env`-Datei
3. Fügen Sie die Konfiguration zum MCP-Client hinzu.

## Verfügbare MCP-Tools
- `local_card_diagnostics(number: str)`: KOSTENLOSES Offline-Tool.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## Preise & Limits
| Plan | Preis | Limit | Monatliches Kontingent |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | Unbegrenzt |


---
*Built for the Model Context Protocol.*