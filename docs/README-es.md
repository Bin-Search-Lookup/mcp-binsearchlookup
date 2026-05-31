# Servidor MCP BinSearchLookup

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

El servidor oficial del Protocolo de Contexto de Modelos (MCP) para [BinSearchLookup.com](https://www.binsearchlookup.com/). Este servidor permite a los agentes de IA (como Claude Desktop, Cursor y LLMs personalizados) interactuar de forma fluida y segura con la API de BinSearchLookup para realizar búsquedas avanzadas de Números de Identificación Bancaria (BIN), análisis de fraude y auditorías masivas de tarjetas.

## Funciones Empresariales
- **Diagnósticos locales sin conexión:** Identifica redes y realiza comprobaciones locales del algoritmo de Luhn en PANs completos de 16 dígitos.
- **Fragmentación automática y concurrencia:** Envíe miles de BIN a la vez.
- **Almacenamiento en caché LRU en memoria:** Ahorra créditos de API.
- **Saneamiento estricto de entradas:** Elimina guiones, letras y espacios en blanco.
- **Resiliencia:** Retroceso exponencial incorporado.
- **Implementación sin instalación:** Ejecute dentro de un contenedor Docker.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).