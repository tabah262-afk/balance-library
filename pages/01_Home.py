import streamlit as st

st.title("🏠 Home")

st.subheader("Selamat Datang di Balance Library")

st.write("""
Balance Library merupakan aplikasi perpustakaan digital yang membantu pengguna
mencari, membaca, dan mengelola koleksi buku secara mudah.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("📚 Koleksi Buku", "1.250+")

with col2:
    st.metric("👥 Pengguna", "350+")

st.divider()

st.subheader("✨ Fitur Utama")

col1, col2 = st.columns(2)

with col1:
    st.info("📚 Ribuan koleksi buku")

    st.info("🔍 Pencarian cepat")

with col2:
    st.info("📖 Baca kapan saja")

    st.info("👤 Kelola akun pengguna")