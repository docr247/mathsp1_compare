import streamlit as st
import time

m = st.markdown("""
<style>
div.stButton > button:first-child {
    font-size: 48px;
    padding: 20px 40px;
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

num1 = 7
num2 = 2

st.write("")
st.markdown("<h2 style='text-align: center;'>Which number is Bigger?</h2>", unsafe_allow_html=True)

col_b1, col_e, col_b2 = st.columns([1.5, 0.2, 1.5])

with col_b1:
    num1_click = st.button(f"{num1}", use_container_width=True)

with col_b2:
    num2_click = st.button(f"{num2}", use_container_width=True)

placeholder2 = st.empty()
placeholder = st.empty()

if num1_click:
    placeholder2.markdown(f"<h2 style='text-align: center;'>{num1} is bigger than {num2}</h2>", unsafe_allow_html=True)
    placeholder.success('Well Done!', icon="✅")
    st.balloons()
if num2_click:
    placeholder.error("Please Try Again!", icon="❌")

time.sleep(2)
placeholder.empty()
placeholder2.empty()
