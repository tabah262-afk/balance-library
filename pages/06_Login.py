import streamlit as st

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

st.button("Masuk")