**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# خادم MCP BinSearchLookup

خادم Model Context Protocol (MCP) الرسمي لـ [BinSearchLookup.com](https://www.binsearchlookup.com/).

يسمح لوكلاء الذكاء الاصطناعي بالتفاعل بأمان مع واجهة برمجة التطبيقات لإجراء عمليات بحث BIN المتقدمة وتحليل الاحتيال وعمليات التدقيق المجمعة.

## ميزات المؤسسة

- **تشخيصات محلية دون اتصال وفحوصات مسبقة:** يحدد الشبكات ويتحقق من خوارزمية Luhn محليًا لتوفير الحصة.
- **التقسيم التلقائي والتزامن:** إرسال آلاف أرقام BIN في وقت واحد.
- **التخزين المؤقت LRU في الذاكرة:** يتم تقديم الطلبات المكررة على الفور من الذاكرة.
- **تطهير صارم للمدخلات:** ينظف المدخلات الفوضوية تلقائيًا.
- **المرونة:** تراجع أسي مدمج.
- **نشر بدون تثبيت:** يعمل بالكامل عبر Docker.

## التثبيت والاستخدام

### الخيار 1: Docker (موصى به)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_مفتاح_api_الخاص_بك",
        "-e", "BSL_USER_ID=معرف_المستخدم_الخاص_بك",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### الخيار 2: Python المحلي
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. تكوين ملف `.env`
3. أضف إلى تكوين عميل MCP الخاص بك.

## أدوات MCP المتاحة
- `local_card_diagnostics(number: str)`: أداة مجانية دون اتصال بالإنترنت.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## الأسعار والحدود
| الخطة | السعر | حد المعدل | الحصة الشهرية |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | غير محدود |


---
*Built for the Model Context Protocol.*