import streamlit as st

def show():

    st.title("👤 Profil")

    st.write("Silakan masuk untuk menggunakan fitur aplikasi.")

    col1, col2 = st.columns(2)

    with col1:
        st.button("Sign In")

    with col2:
        st.button("Sign Up")