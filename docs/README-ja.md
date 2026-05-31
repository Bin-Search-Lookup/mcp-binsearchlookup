**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# BinSearchLookup MCP サーバー

[BinSearchLookup.com](https://www.binsearchlookup.com/) の公式 Model Context Protocol (MCP) サーバーです。

AI エージェントが API と安全に連携し、高度な BIN 検索、不正分析、一括監査を行えるようにします。

## エンタープライズ機能

- **ローカルオフライン診断と事前チェック：** ネットワークを特定し、ローカルで Luhn アルゴリズムを検証してクォータを節約します。
- **自動チャンク化と並行処理：** 一度に何千もの BIN を送信できます。
- **インメモリ LRU キャッシュ：** 重複するリクエストはキャッシュから即座に返されます。
- **厳密な入力サニタイズ：** 乱雑な入力を自動的にクリーンアップします。
- **回復力：** 組み込みの指数バックオフ。
- **ゼロインストールデプロイメント：** Docker 経由で実行。

## インストールと使用方法

### オプション 1: Docker (推奨)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_あなたの_api_key",
        "-e", "BSL_USER_ID=あなたの_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### オプション 2: ローカル Python
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. `.env` ファイルを設定
3. MCP クライアント構成に追加します。

## 利用可能な MCP ツール
- `local_card_diagnostics(number: str)`: 無料のオフラインツール。
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## 料金と制限
| プラン | 料金 | レート制限 | 月間クォータ |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | 無制限 |


---
*Built for the Model Context Protocol.*