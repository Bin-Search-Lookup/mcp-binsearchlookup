**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# Servidor MCP BinSearchLookup

El servidor oficial Model Context Protocol (MCP) para [BinSearchLookup.com](https://www.binsearchlookup.com/).

Permite a los agentes de IA interactuar de forma segura con la API de BinSearchLookup para búsquedas avanzadas de BIN, análisis de fraude y auditorías masivas.

## Funciones Empresariales

- **Diagnósticos Locales y Comprobaciones Previas:** Identifica redes y realiza la validación de Luhn localmente. Los números inválidos se bloquean antes de enviarse a la API.
- **Fragmentación Automática y Concurrencia:** Envíe miles de BIN a la vez sin superar los límites.
- **Caché LRU en Memoria:** Las consultas duplicadas se sirven al instante desde la memoria.
- **Saneamiento Estricto:** Limpia los datos de entrada desordenados de la IA.
- **Resiliencia:** Retroceso exponencial integrado.
- **Despliegue sin Instalación:** Ejecute completamente mediante Docker.

## Instalación y Uso

### Opción 1: Docker (Recomendado)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_tu_clave_api",
        "-e", "BSL_USER_ID=tu_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### Opción 2: Python Local
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. Configurar el archivo `.env`
3. Añadir ruta a la configuración de cliente MCP.

## Herramientas MCP Disponibles
- `local_card_diagnostics(number: str)`: Herramienta GRATUITA sin conexión.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## Precios y Límites
| Plan | Precio | Límite | Cuota Mensual |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | Ilimitado |


---
*Built for the Model Context Protocol.*