# Server MCP BinSearchLookup

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

Il server ufficiale Model Context Protocol (MCP) per [BinSearchLookup.com](https://www.binsearchlookup.com/). Questo server consente agli agenti AI (come Claude Desktop, Cursor e LLM personalizzati) di interfacciarsi in modo fluido e sicuro con l'API BinSearchLookup per eseguire ricerche avanzate di Bank Identification Number (BIN), analisi delle frodi e controlli massivi delle carte.

## Funzionalità Enterprise
- **Diagnostica locale offline:** Identifica le reti ed esegue controlli locali dell'algoritmo di Luhn su PAN completi di 16 cifre.
- **Chunking automatico e concorrenza:** Invia migliaia di BIN in una volta sola.
- **Caching LRU in memoria:** Risparmia i crediti API.
- **Igienizzazione rigorosa degli input:** Rimuove trattini, lettere e spazi bianchi.
- **Resilienza:** Backoff esponenziale integrato.
- **Distribuzione Zero-Install:** Esegui tutto all'interno di un container Docker.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).