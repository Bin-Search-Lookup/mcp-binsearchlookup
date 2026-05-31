# BinSearchLookup MCP 服务器

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

官方的 [BinSearchLookup.com](https://www.binsearchlookup.com/) 模型上下文协议 (MCP) 服务器。该服务器允许 AI 代理（如 Claude Desktop、Cursor 和自定义 LLM）无缝、安全地与 BinSearchLookup API 交互，执行高级的银行识别码 (BIN) 查询、欺诈分析和批量卡片审计。

## 企业功能
- **本地离线诊断：** 识别网络并对完整的 16 位 PAN 进行本地 Luhn 算法检查。
- **自动分块和并发：** 一次提交数千个 BIN。
- **内存 LRU 缓存：** 节省您的 API 额度。
- **严格的输入清理：** 自动去除破折号、字母和空格。
- **弹性：** 内置指数退避算法。
- **零安装部署：** 在轻量级 Docker 容器内运行。

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).