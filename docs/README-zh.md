**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# BinSearchLookup MCP 服务器

官方的 [BinSearchLookup.com](https://www.binsearchlookup.com/) 模型上下文协议 (MCP) 服务器。

允许 AI 代理安全地与 API 交互，进行高级 BIN 查询、欺诈分析和批量审计。

## 企业功能

- **本地离线诊断与预检：** 识别网络并在本地验证 Luhn 算法，以节省配额。
- **自动分块与并发：** 一次发送数千个 BIN。
- **内存 LRU 缓存：** 重复的请求会立即从内存中响应。
- **严格输入清理：** 自动清理混乱的输入。
- **弹性：** 内置指数退避算法以应对限流。
- **零安装部署：** 使用 Docker 运行。

## 安装与使用

### 选项 1：Docker（推荐）

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_你的_api_key",
        "-e", "BSL_USER_ID=你的_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### 选项 2：本地 Python
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. 配置 `.env` 文件
3. 添加到 MCP 客户端配置中。

## 可用的 MCP 工具
- `local_card_diagnostics(number: str)`: 免费的离线诊断工具。
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## 定价与限制
| 套餐 | 价格 | 速率限制 | 月度配额 |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | 无限制 |


---
*Built for the Model Context Protocol.*