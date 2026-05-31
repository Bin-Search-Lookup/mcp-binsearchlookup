# خادم MCP BinSearchLookup

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

خادم Model Context Protocol (MCP) الرسمي لـ [BinSearchLookup.com](https://www.binsearchlookup.com/). يتيح هذا الخادم لعملاء الذكاء الاصطناعي (مثل Claude Desktop و Cursor و LLMs المخصصة) التفاعل بسلاسة وأمان مع واجهة برمجة تطبيقات BinSearchLookup لإجراء عمليات بحث متقدمة عن رقم تعريف البنك (BIN) وتحليل الاحتيال وتدقيق البطاقات المجمعة.

## ميزات المؤسسة
- **تشخيصات محلية دون اتصال:** تحديد الشبكات وإجراء فحوصات خوارزمية Luhn المحلية على أرقام PAN المكونة من 16 رقمًا.
- **التقسيم التلقائي والتزامن:** إرسال آلاف أرقام BIN في وقت واحد.
- **التخزين المؤقت LRU في الذاكرة:** يوفر أرصدة API الخاصة بك.
- **تطهير صارم للمدخلات:** يزيل الشرطات والأحرف والمسافات.
- **المرونة:** تراجع أسي مدمج.
- **نشر بدون تثبيت:** يعمل بالكامل داخل حاوية Docker.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).