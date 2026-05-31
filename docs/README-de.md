# BinSearchLookup MCP-Server

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

Der offizielle Model Context Protocol (MCP)-Server für [BinSearchLookup.com](https://www.binsearchlookup.com/). Dieser Server ermöglicht es KI-Agenten (wie Claude Desktop, Cursor und benutzerdefinierten LLMs), nahtlos und sicher mit der BinSearchLookup-API zu interagieren, um erweiterte Bank Identification Number (BIN)-Suchen, Betrugsanalysen und Massenprüfungen von Karten durchzuführen.

## Enterprise-Funktionen
- **Lokale Offline-Diagnose:** Identifiziert Netzwerke und führt lokale Luhn-Algorithmusprüfungen für vollständige 16-stellige PANs durch.
- **Automatisches Chunking und Nebenläufigkeit:** Senden Sie Tausende von BINs gleichzeitig.
- **In-Memory-LRU-Caching:** Spart API-Guthaben.
- **Strenge Eingabebereinigung:** Entfernt Bindestriche, Buchstaben und Leerzeichen.
- **Ausfallsicherheit:** Integrierter exponentieller Backoff.
- **Zero-Install Deployment:** Komplett im Docker-Container ausführen.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).