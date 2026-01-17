# 🌸 WithSlide - P2P Anonymous Q&A Platform

ブラウザベースのP2P匿名Q&Aプラットフォームです。WebRTCを使用してホストとゲスト間で直接通信し、リアルタイムで質問の投稿・いいね・回答管理ができます。

![Dark Mode Web App](https://img.shields.io/badge/Theme-Dark%20Mode-1a1a2e)
![WebRTC](https://img.shields.io/badge/Protocol-WebRTC-00d4ff)
![Python](https://img.shields.io/badge/Server-Python%203.8%2B-ff6b9d)

## ✨ 特徴

- **完全P2P通信**: サーバーレスでプライバシー重視
- **自動シグナリング**: IPアドレスとルームIDで簡単接続
- **リアルタイム同期**: 質問・いいね・回答状態が即座に反映
- **ダークモード対応**: 目に優しいUI
- **絵文字リアクション**: 履歴機能付き絵文字ピッカー
- **データ保存/読込**: JSONでセッションデータをエクスポート/インポート

---

## 📋 必要な実行環境

### シグナリングサーバー (Python)

| 項目 | 要件 |
|------|------|
| Python | 3.8 以上 |
| ライブラリ | `websockets` |
| ポート | 8765 (変更可能) |

### クライアント (ブラウザ)

| 項目 | 要件 |
|------|------|
| ブラウザ | Chrome, Edge, Firefox (最新版推奨) |
| プロトコル | HTTP または HTTPS |
| WebRTC | 対応必須 |

---

## 🚀 セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/yourusername/withslide.git
cd withslide
```

### 2. Python依存関係をインストール

```bash
pip install websockets
```

### 3. シグナリングサーバーを起動

```bash
python server.py
```

> サーバーは `ws://0.0.0.0:8765` で起動します。
> 同じネットワーク内の他のデバイスからもアクセス可能です。

### 4. クライアントを開く

`index.html` をブラウザで開きます。

- ローカル: `file:///path/to/withslide/index.html`
- サーバー経由: `http://localhost:5500/index.html` (Live Serverなど)

---

## 📖 使い方

### ホストとして開始

1. 「**ホストとして開始**」をクリック
2. シグナリングサーバーのIPアドレスを入力 (例: `192.168.1.100`)
3. 「**開始**」をクリック
4. 表示された接続情報 (例: `192.168.1.100:1234`) をゲストに共有

### ゲストとして参加

1. 「**ゲストとして参加**」をクリック
2. ホストから受け取った接続情報を入力 (例: `192.168.1.100:1234`)
3. 「**接続開始**」をクリック

---

## 📁 ファイル構成

```
withslide/
├── index.html      # メインアプリケーション (HTML/CSS/JS統合)
├── server.py       # Pythonシグナリングサーバー
└── README.md       # このファイル
```

---

## 🔧 設定

### ポート変更

`server.py` の以下の行を編集:

```python
server = await websockets.serve(signaling_handler, "0.0.0.0", 8765)
```

ポート `8765` を任意の値に変更してください。

---

## 🎨 スクリーンショット

### 接続フロー

| ホスト | ゲスト |
|--------|--------|
| IP入力 → 開始 → 接続情報表示 | 接続情報入力 → 接続開始 |

---

## 📄 ライセンス

🍣 **Sushi-ware License**

このソフトウェアは Sushi-ware ライセンスの下で公開されています。
このソフトウェアが気に入ったら、作者にお寿司を奢ってください！🍣

```
"THE SUSHI-WARE LICENSE" (Revision 42):
このソフトウェアを自由に使用・複製・改変・配布できます。
もしこのソフトウェアが気に入ったら、いつか会った時にお寿司を奢ってください。
```

---

## 🤝 貢献

Issue や Pull Request は大歓迎です！

---

## 📞 お問い合わせ

何かご質問があれば、Issueを作成してください。
