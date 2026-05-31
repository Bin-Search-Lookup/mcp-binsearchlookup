# BinSearchLookup MCP 서버

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

[BinSearchLookup.com](https://www.binsearchlookup.com/)의 공식 Model Context Protocol (MCP) 서버입니다. 이 서버를 통해 AI 에이전트(Claude Desktop, Cursor 및 사용자 정의 LLM)가 BinSearchLookup API와 원활하고 안전하게 상호 작용하여 고급 은행 식별 번호(BIN) 조회, 사기 분석 및 대량 카드 감사를 수행할 수 있습니다.

## 엔터프라이즈 기능
- **로컬 오프라인 진단:** 네트워크를 식별하고 전체 16자리 PAN에 대해 로컬로 룬(Luhn) 알고리즘 검사를 수행합니다.
- **자동 청킹 및 동시성:** 한 번에 수천 개의 BIN을 제출합니다.
- **인메모리 LRU 캐싱:** API 크레딧을 절약합니다.
- **엄격한 입력 삭제:** 대시, 문자 및 공백을 자동으로 제거합니다.
- **복원력:** 내장된 지수 백오프.
- **무설치 배포:** Docker 컨테이너 내부에서 완전히 실행합니다.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).