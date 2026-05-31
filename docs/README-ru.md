**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# Сервер MCP BinSearchLookup

Официальный сервер Model Context Protocol (MCP) для [BinSearchLookup.com](https://www.binsearchlookup.com/).

Позволяет ИИ-агентам безопасно взаимодействовать с API для расширенного поиска BIN, анализа мошенничества и массовых проверок.

## Корпоративные функции

- **Локальная автономная диагностика:** Определяет сети и выполняет локальные проверки алгоритма Луна для экономии квот.
- **Автоматическое разделение:** Отправляйте тысячи BIN одновременно.
- **Кэширование LRU в памяти:** Дублирующиеся запросы мгновенно обрабатываются из памяти.
- **Строгая очистка:** Автоматически очищает входные данные.
- **Отказоустойчивость:** Встроенная экспоненциальная задержка.
- **Развертывание без установки:** Используйте Docker.

## Установка и Использование

### Вариант 1: Docker (Рекомендуется)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_ваш_api_ключ",
        "-e", "BSL_USER_ID=ваш_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### Вариант 2: Локальный Python
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. Настройте файл `.env`
3. Добавьте в конфигурацию MCP-клиента.

## Доступные инструменты MCP
- `local_card_diagnostics(number: str)`: БЕСПЛАТНЫЙ автономный инструмент.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## Цены и Лимиты
| План | Цена | Лимит | Месячная квота |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | Безлимит |


---
*Built for the Model Context Protocol.*