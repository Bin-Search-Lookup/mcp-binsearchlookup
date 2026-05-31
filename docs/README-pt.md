**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# Servidor MCP BinSearchLookup

O servidor oficial Model Context Protocol (MCP) para [BinSearchLookup.com](https://www.binsearchlookup.com/).

Permite que agentes de IA interajam de forma segura com a API para pesquisas avançadas de BIN, análises de fraude e auditorias em massa.

## Recursos Enterprise

- **Diagnóstico Local e Verificações Prévias:** Identifica redes e realiza a validação de Luhn localmente.
- **Fragmentação Automática e Concorrência:** Envie milhares de BINs de uma vez.
- **Cache LRU na Memória:** Solicitações duplicadas são atendidas instantaneamente.
- **Limpeza Rigorosa:** Limpa entradas desordenadas.
- **Resiliência:** Backoff exponencial integrado.
- **Implantação Zero-Install:** Execute usando Docker.

## Instalação e Uso

### Opção 1: Docker (Recomendado)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_sua_api_key",
        "-e", "BSL_USER_ID=seu_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### Opção 2: Python Local
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. Configure o arquivo `.env`
3. Adicione à configuração do cliente MCP.

## Ferramentas MCP Disponíveis
- `local_card_diagnostics(number: str)`: Ferramenta offline GRATUITA.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## Preços e Limites
| Plano | Preço | Limite | Cota Mensal |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | Ilimitado |


---
*Built for the Model Context Protocol.*