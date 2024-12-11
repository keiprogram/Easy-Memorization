import streamlit as st
import pandas as pd
import random

# アプリのタイトル
st.title("暗記学習アプリ")

# Excelファイルのアップロード
uploaded_file = st.file_uploader("学習用のExcelファイルをアップロードしてください", type=["xlsx"])

if uploaded_file:
    # アップロードされたファイルをデータフレームとして読み込み
    df = pd.read_excel(uploaded_file)

    # 必要なカラムがあるか確認
    if "問題" in df.columns and "解答" in df.columns:
        st.success("ファイルの読み込みに成功しました！")
        
        # 問題をランダムに出題
        if st.button("問題を出題"):
            question = df.sample(1).iloc[0]
            st.write(f"**問題:** {question['問題']}")
            
            # 解答入力
            user_answer = st.text_input("あなたの解答を入力してください")

            if st.button("解答を確認"):
                correct_answer = question['解答']
                if user_answer.strip() == correct_answer.strip():
                    st.success("正解です！")
                else:
                    st.error(f"不正解です。正しい答えは: {correct_answer}")
    else:
        st.error("Excelファイルには '問題' と '解答' カラムが必要です。")

# ヒント
st.info("ヒント: Excelファイルには '問題' と '解答' という列名が必要です。")
