**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# BinSearchLookup MCP 서버

[BinSearchLookup.com](https://www.binsearchlookup.com/)의 공식 Model Context Protocol (MCP) 서버입니다.

AI 에이전트가 API와 안전하게 상호 작용하여 고급 BIN 검색, 사기 분석 및 대량 감사를 수행할 수 있도록 합니다.

## 엔터프라이즈 기능

- **로컬 오프라인 진단 및 사전 검사:** 할당량을 절약하기 위해 네트워크를 식별하고 로컬에서 룬(Luhn) 알고리즘을 확인합니다.
- **자동 청킹 및 동시성:** 한 번에 수천 개의 BIN을 제출합니다.
- **인메모리 LRU 캐싱:** 중복 요청은 즉시 메모리에서 제공됩니다.
- **엄격한 입력 삭제:** 지저분한 입력을 자동으로 정리합니다.
- **복원력:** 내장된 지수 백오프.
- **무설치 배포:** Docker를 통해 완전히 실행.

## 설치 및 사용

### 옵션 1: Docker (권장)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_귀하의_api_key",
        "-e", "BSL_USER_ID=귀하의_user_id",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### 옵션 2: 로컬 Python
1. `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. `.env` 파일 구성
3. MCP 클라이언트 구성에 추가합니다.

## 사용 가능한 MCP 도구
- `local_card_diagnostics(number: str)`: 무료 오프라인 도구.
- `lookup_bin(bin_number: str)`
- `batch_lookup_bins(bins: List[str])`
- `check_quota(public_user_id: str)`
- `check_system_health()`

## 가격 및 제한
| 요금제 | 가격 | 속도 제한 | 월간 할당량 |
|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 |
| **Enterprise** | $999 / $980 | 768 req/min | 무제한 |


---
*Built for the Model Context Protocol.*