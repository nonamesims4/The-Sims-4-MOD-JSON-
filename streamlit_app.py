import streamlit as st
import json
import re
from deep_translator import GoogleTranslator
import time
import io

# ページ設定
st.set_page_config(
    page_title="The Sims 4 MOD JSON翻訳ツール",
    page_icon="🎮",
    layout="wide"
)

# タイトル
st.title("🎮 The Sims 4 MOD JSON翻訳ツール")
st.markdown("---")

# プレースホルダー（{}で囲まれたタグ）を安全なトークンに置換して保護する関数
def mask_placeholders(text):
    pattern = r'\{[0-9a-zA-Z\._]+\}'
    found = re.findall(pattern, text)
    masked = text
    placeholder_map = {}
    for i, ph in enumerate(found):
        token = f'__PH_{i}__'
        masked = masked.replace(ph, token, 1)
        placeholder_map[token] = ph
    return masked, placeholder_map

# 翻訳後にトークンを元のプレースホルダー（タグ）に戻す関数
def unmask_placeholders(text, placeholder_map):
    for token, ph in placeholder_map.items():
        text = text.replace(token, ph)
    return text

# タグ置換辞書
replace_dict = {
    # 大文字タグ（公式MODでメイン）
    '{M0.he}': '{M0.彼}',
    '{M0.his}': '{M0.彼の}',
    '{F0.she}': '{F0.彼女}',
    '{F0.her}': '{F0.彼女の}',
    '{M1.he}': '{M1.彼}',
    '{M1.his}': '{M1.彼の}',
    '{F1.she}': '{F1.彼女}',
    '{F1.her}': '{F1.彼女の}',

    # 小文字タグがあれば大文字タグに置換
    '{m0.he}': '{M0.彼}',
    '{m0.his}': '{M0.彼の}',
    '{f0.she}': '{F0.彼女}',
    '{f0.her}': '{F0.彼女の}',
    '{m1.he}': '{M1.彼}',
    '{m1.his}': '{M1.彼の}',
    '{f1.she}': '{F1.彼女}',
    '{f1.her}': '{F1.彼女の}',

    # タグ表記修正（必ず大文字）
    '{0.simfirstname}': '{0.SimFirstName}',
    '{1.simfirstname}': '{1.SimFirstName}',

    # SimPronoun系タグ（大文字統一）
    '{0.SimPronounSubjective}': '{M0.彼}{F0.彼女}',
    '{0.SimPronounPossessiveDependent}': '{M0.彼}{F0.彼女}',
    '{0.SimPronounReflexive}': '{M0.彼}{F0.彼女}',
    '{0.SimPronounObjective}': '{M0.彼}{F0.彼女}',

    # 同性連続プレースホルダーの不自然連結を自然に直す（大文字版）
    '{F0.彼女の}{F0.彼女}': '{F0.彼女}',
    '{F0.彼女}{F0.彼女の}': '{F0.彼女}',
    '{M0.彼の}{M0.彼}': '{M0.彼}',
    '{M0.彼}{M0.彼の}': '{M0.彼}',

    # 二重助詞「の」対策
    '{F0.彼女の}の本': '{F0.彼女}の本',
    '{M0.彼の}の家': '{M0.彼}の家',

    # 助詞の二重連結対策（に、が、は、を、など）
    '{F0.彼女に}に本': '{F0.彼女}に本',
    '{M0.彼に}に家': '{M0.彼}に家',
    '{F0.彼女が}が本': '{F0.彼女}が本',
    '{M0.彼が}が家': '{M0.彼}が家',
    '{F0.彼女は}は本': '{F0.彼女}は本',
    '{M0.彼は}は家': '{M0.彼}は家',
    '{F0.彼女を}を本': '{F0.彼女}を本',
    '{M0.彼を}を家': '{M0.彼}を家',
    '{F0.彼女と}と友達': '{F0.彼女}と友達',
    '{M0.彼と}と友達': '{M0.彼}と友達',

    # 複数連続タグの簡素化例
    '{F0.彼女の}{F0.彼女}は遊びに行った': '{F0.彼女}は遊びに行った',
    '{M0.彼の}{M0.彼}は来なかった': '{M0.彼}は来なかった',
}

# テキスト内のタグを置換辞書に従い置換していく関数
def normalize_tags(text):
    for k, v in replace_dict.items():
        text = text.replace(k, v)
    return text

# テキストに日本語（ひらがな・カタカナ・漢字）が含まれているか判定
def is_japanese(text):
    if not text:
        return False
    return bool(re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', text))

# 安全に翻訳しつつリトライを行う関数
def safe_translate(text, src='en', dest='ja', max_retries=3):
    if not text.strip():
        return text
    
    for attempt in range(max_retries):
        try:
            # deep-translator使用（より安定）
            translator = GoogleTranslator(source=src, target=dest)
            result = translator.translate(text)
            
            if result:
                return result
                    
        except Exception as e:
            # エラーログを表示しない（静かに失敗）
            time.sleep(1 + attempt)
                    
    # 翻訳失敗時は元のテキストを返す
    return text

# 長文を最大長さ(maxlen)ごとに分割し分割翻訳する関数
def translate_long_text(text, src='en', dest='ja', maxlen=4500):
    if len(text) <= maxlen:
        return safe_translate(text, src, dest)
    sentences = re.split(r'(?<=[.!?。！？\n])', text)
    out = ''
    buf = ''
    for s in sentences:
        if len(buf) + len(s) > maxlen:
            out += safe_translate(buf, src, dest)
            buf = s
        else:
            buf += s
    if buf:
        out += safe_translate(buf, src, dest)
    return out

# メイン処理関数
def process_json_file(uploaded_file):
    try:
        # JSONファイルを読み込み
        data = json.loads(uploaded_file.read().decode('utf-8'))
        
        # 翻訳処理
        translated_count = 0
        skipped_count = 0
        
        # プログレスバーを表示
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_entries = len(data)
        
        for idx, entry in enumerate(data):
            val = entry.get('value', '')
            if not val:
                continue
                
            if is_japanese(val):
                skipped_count += 1
                continue
            
            # 進捗更新
            progress = (idx + 1) / total_entries
            progress_bar.progress(progress)
            status_text.text(f'翻訳中 [{idx+1}/{total_entries}]: {val[:40]}{"..." if len(val) > 40 else ""}')
            
            # 翻訳処理
            masked, placeholder_map = mask_placeholders(val)
            translated = translate_long_text(masked)
            restored = unmask_placeholders(translated, placeholder_map)
            fixed = normalize_tags(restored)
            entry['value'] = fixed
            
            translated_count += 1
            time.sleep(0.5)  # APIへの負荷軽減（4.0.0rc1は安定）
        
        # 完了メッセージ
        status_text.text(f'翻訳完了: {translated_count}件翻訳、{skipped_count}件スキップ')
        progress_bar.progress(1.0)
        
        return data, translated_count, skipped_count
        
    except json.JSONDecodeError:
        st.error("❌ 無効なJSONファイルです。正しいJSONファイルをアップロードしてください。")
        return None, 0, 0
    except Exception as e:
        st.error(f"❌ ファイル処理中にエラーが発生しました: {e}")
        return None, 0, 0

# メインアプリケーション
def main():
    # 説明文
    st.markdown("""
    このツールは **The Sims 4 MOD用JSONファイル** を自動で日本語に翻訳します。
    
    ### 🔧 機能
    - 📤 JSONファイルのアップロード
    - 🔄 英語から日本語への自動翻訳
    - 🛡️ タグ保護機能（{M0.he}、{F0.she}などのプレースホルダー保護）
    - 📝 MOD固有のタグ置換による自然な日本語化
    - 📊 翻訳進捗のリアルタイム表示
    - ⏭️ 日本語テキストの自動スキップ
    - 📥 翻訳済みファイルのダウンロード
    
    ### 📋 使用方法
    1. 下のファイルアップローダーからJSONファイルを選択
    2. 自動で翻訳処理が開始されます
    3. 処理完了後、翻訳されたファイルをダウンロード
    """)
    
    st.markdown("---")
    
    # ファイルアップローダー
    uploaded_file = st.file_uploader(
        "📁 The Sims 4 MOD用JSONファイルを選択してください",
        type=['json'],
        help="シムズ4のMOD用JSONファイル（英語）をアップロードしてください"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ ファイル '{uploaded_file.name}' がアップロードされました")
        
        # 翻訳開始ボタン
        if st.button("🚀 翻訳を開始", type="primary"):
            with st.spinner("翻訳処理を実行中..."):
                # ファイルを処理
                translated_data, translated_count, skipped_count = process_json_file(uploaded_file)
                
                if translated_data is not None:
                    # 結果の表示
                    st.success("🎉 翻訳が完了しました！")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("翻訳された項目", translated_count)
                    with col2:
                        st.metric("スキップされた項目", skipped_count)
                    
                    # 翻訳結果をJSONに変換
                    translated_json = json.dumps(translated_data, ensure_ascii=False, indent=2)
                    
                    # ダウンロードボタン
                    st.download_button(
                        label="📥 翻訳済みJSONファイルをダウンロード",
                        data=translated_json,
                        file_name=f"translated_{uploaded_file.name}",
                        mime="application/json",
                        type="primary"
                    )
                    
                    # プレビュー表示（最初の5項目）
                    with st.expander("📋 翻訳結果プレビュー（最初の5項目）"):
                        preview_data = translated_data[:5] if len(translated_data) > 5 else translated_data
                        for i, item in enumerate(preview_data):
                            if 'value' in item and item['value']:
                                st.write(f"**項目 {i+1}:** {item['value']}")
    
    # サイドバーに追加情報
    with st.sidebar:
        st.header("ℹ️ 詳細情報")
        st.markdown("""
        ### 🎯 対応タグ
        - `{M0.he}` → `{M0.彼}`
        - `{F0.she}` → `{F0.彼女}`
        - `{M0.his}` → `{M0.彼の}`
        - `{F0.her}` → `{F0.彼女の}`
        - その他多数のタグに対応
        
        ### ⚠️ 注意事項
        - 翻訳にはGoogle翻訳を使用
        - 大容量ファイルは処理に時間がかかります
        - 既に日本語のテキストは自動でスキップされます
        
        ### 🛠️ 技術仕様
        - deep-translator使用（最安定版）
        - プレースホルダー保護機能
        - 長文分割翻訳対応
        - 静かなエラーハンドリング（ログ非表示）
        """)

if __name__ == "__main__":
    main()
