このツールについて

このツールはTheSims4MOD用のJSONファイルを自動で日本語に翻訳しながら{M0.he}、{F0.she} などのプレースホルダーを {M0.彼}、{F0.彼女}に変換できるツールです。翻訳後でも{M0.he}、{F0.she} を {M0.彼}、{F0.彼女}に変換できます。  
🆕翻訳なしで{M0.he}、{F0.she} を {M0.彼}、{F0.彼女}に変換だけしたい人専用ツールできました→<a href="https://nonamesims4.github.io/The-Sims-4-MOD-JSON-/" target="_blank" rel="noopener noreferrer">Sims4Translator対応JSONファイルプレースホルダー置換ツール</a>    
🆕<a href="https://github.com/voky1" target="_blank" rel="noopener noreferrer">TheSims4Translator</a>から出力される"Entries" 構造対応のjsonファイルに対応できるようになりました。出力後のJSONファイルは他ツールに使用できます。 


🔄 JSONファイルの変換はこちらのサイトやソフトを利用してください：  
🌐 <a href="https://stbl.sims4toolkit.com/" target="_blank" rel="noopener noreferrer">STBL Studio</a>  
🌐 <a href="https://github.com/voky1" target="_blank" rel="noopener noreferrer">TheSims4Translator</a>


🔧 機能

- 📤 JSONファイルのアップロード
- 🔄 英語から日本語への自動翻訳
- 🔧 翻訳済みファイルのプレースホルダー翻訳
- ✨ s4 stbl mergeを使った翻訳後の先頭アスタリスク削除
- 🛡️ タグ保護機能（{M0.he}、{F0.she}などのプレースホルダー保護）
- 📝 MOD固有のタグ置換による自然な日本語化
- 📊 翻訳進捗のリアルタイム表示
- ⏭️ 日本語テキストの自動スキップ
- 📥 翻訳済みファイルのダウンロード
- 🌍"Entries" 構造対応のjsonファイルに対応



ℹ️ 対応タグ例
- {M0.he}   → {M0.彼} 
- {F0.she}  → {F0.彼女}
- {M0.his}  → {M0.彼の}
- {F0.her}  → {F0.彼女の}  

その他、多数のタグに対応しています。


⚠️ 注意事項

- 翻訳には deep-translator API を使用しています
- 翻訳の行数によっては処理に時間がかかる場合があります
- 日本語のテキストは自動でスキップされますが、タグ置換とアスタリスク削除は実行されます
- 出力後に`__PH_0__` や `__PH_1__`といったトークンが出る場合があります→ jsonファイルはテキストで編集が可能です。それぞれ {0.SimFirstName} や {1.SimFirstName} に置き換えてください。（または翻訳ソフト内で修正してください。
- こちらで`__PH_0__` や `__PH_1__`といったトークンが修正できるようになりました→<a href="https://nonamesims4.github.io/The-Sims-4-MOD-JSON-/" target="_blank" rel="noopener noreferrer">Sims4専用JSONファイルタグ置換ツール翻訳なしバージョン</a>


**実行時の警告についてのご案内**

このColabノートブックはGitHubなどGoogle以外のソースから読み込まれているため、Colab上で実行時に以下のような警告メッセージが表示されることがあります。

*「警告: このノートブックは Google が作成したものではありません。悪意のあるコードが含まれている可能性もあります。実行前にソースコードの確認を推奨します。」*

この警告はGoogle側からの標準的な注意喚起であり、ノートブックの内容や安全性を保証するものではありません。
本ツールはThe Sims 4 MODのJSON翻訳処理を目的としており、Google Drive内の個人情報アクセスや外部不正通信は行いません。
安心してご利用いただくために、コードの中身を目を通して理解したうえで実行することをおすすめします。

不安がある場合は、こちらのGitHubリポジトリのページもご確認ください： 🌐https://github.com/nonamesims4/The-Sims-4-MOD-JSON-

🛠️ 技術仕様
- 使用ライブラリ：deep-translator
- プレースホルダー保護機能付き
- 長文翻訳時の自動分割対応
- エラーハンドリング・リトライ機能搭載
- s4 stbl merge対応のアスタリスク削除機能
- 日本語テキストでもタグ置換・アスタリスク削除を実行
- Colabベース

## ❓ よくある質問（FAQ）

**Q. 翻訳したファイルをそのままMODに使っていいの？**  
A. こちらの <a href="https://stbl.sims4toolkit.com/" target="_blank" rel="noopener noreferrer">STBL Studio</a>でstblに変換し保存後、翻訳ソフトで読み込むと翻訳パッケージとして使用できます。念のためバックアップを取ってからの使用をおすすめします。

**Q. 大きなJSONファイルでも変換できる？**  
A. はい、UTF-8形式のJSONファイルなら数千エントリでもOK！(自分が試したのは3000行)ただし、大きなファイルは処理に時間がかかる場合があります。









Special Thanks

このツールの開発にあたり、以下の皆さまに心より感謝いたします。

- 素敵なMODやCCを制作してくださっているクリエイターの皆様  
- 翻訳ソフトを開発してくださったエンジニアの皆様  
- The Sims 4 MODの日本語化方法を共有してくださった方々  
- STBL Studioという素晴らしいサイトを紹介してくださった方
- STBL Studioという素晴らしいサイトを作ってくれたFrankk様
- プレースホルダーの仕組みをわかりやすく解説してくださったブログの運営者様  
- 英語が苦手な私に丁寧に教えてくれた家族
- 技術的なヒントやコードのひな型を提案、提供してくれたAIたち

皆様のおかげで、このツールを完成させることができました。本当にありがとうございます！


そして――  
このツールを見つけてくださった **あなた** に、最大級の感謝を。

