# Сервер MCP BinSearchLookup

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

Официальный сервер Model Context Protocol (MCP) для [BinSearchLookup.com](https://www.binsearchlookup.com/). Этот сервер позволяет ИИ-агентам (таким как Claude Desktop, Cursor и пользовательским LLM) легко и безопасно взаимодействовать с API BinSearchLookup для расширенного поиска банковских идентификационных номеров (BIN), анализа мошенничества и массового аудита карт.

## Корпоративные функции
- **Локальная автономная диагностика:** Определяет сети и выполняет локальные проверки по алгоритму Луна для полных 16-значных PAN.
- **Автоматическое разделение и параллелизм:** Отправляйте тысячи BIN одновременно.
- **Кэширование LRU в памяти:** Экономит кредиты API.
- **Строгая очистка входных данных:** Удаляет тире, буквы и пробелы.
- **Отказоустойчивость:** Встроенная экспоненциальная задержка.
- **Развертывание без установки:** Запускайте внутри контейнера Docker.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).