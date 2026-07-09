import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Balance Library",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Judul
st.title("📚 Balance Library")

st.subheader("Perpustakaan Digital Berbasis Android")

st.write(
    "Selamat datang di Balance Library. "
    "Aplikasi ini memudahkan pengguna untuk mencari, meminjam, "
    "dan mengelola buku secara digital melalui smartphone maupun komputer."
)

st.divider()

st.info("Silakan login untuk melanjutkan.")