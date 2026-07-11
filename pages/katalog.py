import streamlit as st

def show():

    st.title("📚 Katalog Buku")

    with st.expander("📒 Akuntansi"):
        st.write("Pengantar Akuntansi")
        st.write("Intermediate Accounting")

    with st.expander("💰 Perpajakan"):
        st.write("Perpajakan 1")