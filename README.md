# The-Sims-4-MOD-JSON-
The Sims 4 MOD JSON翻訳ツール

# 🎮 The Sims 4 MOD JSON翻訳ツール

シムズ4のMOD用JSONファイルを自動で日本語に翻訳するStreamlitアプリケーションです。

**🌐 https://kekh8hq2caubgxznx6qtqc.streamlit.app/

## ✨ 機能

- 📤 **JSONファイルのアップロード** - ドラッグ&ドロップ対応
- 🔄 **英語から日本語への自動翻訳** - Google翻訳エンジン使用
- 🛡️ **ゲームタグ保護機能** - `{M0.he}`, `{F0.she}`などのプレースホルダー完全保護
- 📝 **MOD固有タグの最適化** - 自然な日本語への変換
- 📊 **リアルタイム進捗表示** - 翻訳状況をリアルタイムで確認
- ⏭️ **日本語テキストの自動スキップ** - 効率的な処理
- 📥 **翻訳済みファイルのダウンロード** - ワンクリックダウンロード

## 🎯 対応タグ例

| 英語タグ | 日本語タグ | 説明 |
|---------|-----------|------|
| `{M0.he}` | `{M0.彼}` | 男性代名詞 |
| `{F0.she}` | `{F0.彼女}` | 女性代名詞 |
| `{M0.his}` | `{M0.彼の}` | 男性所有格 |
| `{F0.her}` | `{F0.彼女の}` | 女性所有格 |

その他50以上のタグパターンに対応

## 🚀 Streamlit Community Cloudでのデプロイ

### 前提条件
- GitHubアカウント
- Streamlit Community Cloudアカウント（GitHubでサインアップ可能）

### デプロイ手順

1. **GitHubリポジトリの作成**
   ```bash
   # 新しいリポジトリを作成し、以下のファイルをアップロード
   - streamlit_app.py
   - packages.txt
   - README.md
   ```

2. **Streamlit Community Cloudでデプロイ**
   - [share.streamlit.io](https://share.streamlit.io) にアクセス
   - GitHubアカウントでサインイン
   - 「New app」をクリック
   - リポジトリとブランチを選択
   - Main file path: `streamlit_app.py`
   - 「Deploy!」をクリック

3. **自動デプロイ完了**
   - 数分でアプリが公開されます
   - 公開URLが生成されます（例: `https://your-app-name.streamlit.app`）

## 💻 ローカル開発

### インストール
```bash
pip install streamlit deep-translator requests
```

### 実行
```bash
streamlit run streamlit_app.py
```

## 🛠️ 技術仕様

- **フレームワーク**: Streamlit 1.28+
- **翻訳エンジン**: deep-translator (Google翻訳)
- **Python**: 3.8+
- **プレースホルダー保護**: 正規表現ベース
- **エラーハンドリング**: 自動リトライ & 静かな失敗

## ⚠️ 注意事項

- 翻訳にはGoogle翻訳を使用
- 大容量ファイルは処理時間がかかります
- 既に日本語のテキストは自動でスキップ
- インターネット接続が必要

## 📝 ライセンス

MIT License - 自由に使用、修正、配布可能

## 🤝 コントリビューション

Issues や Pull Requests を歓迎します！

---

**作成者**: シムズ4コミュニティのために  
**更新日**: 2025年1月
