import streamlit as st

def show():

    kiri, tengah, kanan = st.columns([2,1,2])

    with tengah:

        with tengah:
            st.image(
                "assets/logo.png",
                use_container_width=True
            )

        st.title("Balance Library")

        st.subheader("Perpustakaan Digital Berbasis Android")

        st.markdown("""
### Selamat Datang 👋

**Balance Library** adalah aplikasi perpustakaan digital yang membantu
pengguna menemukan, membaca, dan mengelola koleksi buku dengan mudah.
""")

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.markdown("## 📚")
                st.subheader("Katalog Buku")
                st.caption("Jelajahi seluruh koleksi buku digital.")
                st.button("Buka", key="katalog")

        with col2:
            with st.container(border=True):
                st.markdown("## 📖")
                st.subheader("My Books")
                st.caption("Lihat buku yang telah kamu simpan.")
                st.button("Buka", key="mybooks")

        with col3:
            with st.container(border=True):
                st.markdown("## 👤")
                st.subheader("Profil")
                st.caption("Login dan kelola akun pengguna.")
                st.button("Masuk", key="profil")