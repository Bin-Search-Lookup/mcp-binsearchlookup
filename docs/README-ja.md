# BinSearchLookup MCP サーバー

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

[BinSearchLookup.com](https://www.binsearchlookup.com/) の公式 Model Context Protocol (MCP) サーバーです。このサーバーを使用すると、AIエージェント（Claude Desktop、Cursor、カスタムLLMなど）がBinSearchLookup APIとシームレスかつ安全に連携し、高度な銀行識別番号（BIN）検索、不正分析、一括カード監査を実行できます。

## エンタープライズ機能
- **ローカルオフライン診断：** ネットワークを特定し、16桁の完全なPANに対するLuhnアルゴリズムチェックをローカルで実行します。
- **自動チャンク化と並行処理：** 一度に数千のBINを送信します。
- **インメモリLRUキャッシュ：** APIクレジットを節約します。
- **厳密な入力サニタイズ：** ダッシュ、文字、空白を自動的に削除します。
- **回復力：** 組み込みの指数バックオフ。
- **ゼロインストールデプロイメント：** Dockerコンテナ内で完全に実行します。

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).