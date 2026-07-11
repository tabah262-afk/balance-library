import streamlit as st

def show():

    st.title("🔍 Search")

    keyword=st.text_input("Cari Buku")

    if keyword:
        st.write("Hasil pencarian akan muncul disini.")