**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# Server MCP BinSearchLookup

Il server ufficiale Model Context Protocol (MCP) per [BinSearchLookup.com](https://www.binsearchlookup.com/).

Consente agli agenti AI di interfacciarsi in modo sicuro con l'API per ricerche BIN, analisi frodi e controlli massivi.

## Funzionalità Enterprise

- **Diagnostica Locale Offline:** Identifica le reti e convalida l'algoritmo di Luhn localmente per risparmiare quota.
- **Chunking Automatico e Concorrenza:** Invia migliaia di BIN contemporaneamente.
- **Cache LRU in Memoria:** Le richieste duplicate vengono servite istantaneamente.
- **Pulizia Rigorosa:** Sanitizza gli input automaticamente.
- **Resilienza:** Backoff esponenziale integrato.
- **Deploy Senza Installazione:** Tramite Docker.

## Installazione e Uso

### Opzione 1: Docker (Consigliato)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_tua_api_key",
        "-e", "BSL_USER_ID=tuo_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### Opzione 2: Python Locale
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. Configurare `.env`
3. Aggiungere alla configurazione MCP.

## Strumenti MCP Disponibili
- `local_card_diagnostics(number: str)`: Strumento offline GRATUITO.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## Prezzi e Limiti
| Piano | Prezzo | Limite | Quota Mensile |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | Illimitato |


---
*Built for the Model Context Protocol.*