import streamlit as st

st.title("📚 Katalog Buku")

search = st.text_input("🔍 Cari Judul Buku")

kategori = st.selectbox(
    "Kategori",
    [
        "Semua",
        "Akuntansi",
        "Manajemen",
        "Perpajakan",
        "Keuangan",
        "Bisnis"
    ]
)

st.divider()

st.info("Belum ada data buku.")