import streamlit as st

# セッションステートで入力値と演算状態を管理
if "current_input" not in st.session_state:
    st.session_state.current_input = ""
if "result" not in st.session_state:
    st.session_state.result = None

# 数字ボタンの処理
def add_to_input(value):
    st.session_state.current_input += str(value)

# 計算処理
def calculate():
    try:
        st.session_state.result = eval(st.session_state.current_input)
    except Exception:
        st.session_state.result = "エラー"

# 入力値のクリア
def clear_input():
    st.session_state.current_input = ""
    st.session_state.result = None

# レイアウト（列の幅を調整）
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # すべて均等な幅

# ボタンの配置
with col1:
    if st.button("1"):
        add_to_input(1)
    if st.button("4"):
        add_to_input(4)
    if st.button("7"):
        add_to_input(7)
    if st.button("C"):
        clear_input()

with col2:
    if st.button("2"):
        add_to_input(2)
    if st.button("5"):
        add_to_input(5)
    if st.button("8"):
        add_to_input(8)
    if st.button("0"):
        add_to_input(0)

with col3:
    if st.button("3"):
        add_to_input(3)
    if st.button("6"):
        add_to_input(6)
    if st.button("9"):
        add_to_input(9)
    if st.button("="):
        calculate()

with col4:
    if st.button("＋"):
        add_to_input("+")
    if st.button("－"):
        add_to_input("-")
    if st.button("×"):
        add_to_input("*")
    if st.button("÷"):
        add_to_input("/")

# 現在の入力と結果を表示
st.text_area("入力中の式", value=st.session_state.current_input, height=70)
if st.session_state.result is not None:
    st.write(f"計算結果: {st.session_state.result}")