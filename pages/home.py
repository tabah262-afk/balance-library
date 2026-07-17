import streamlit as st

from database.database import (
    total_books,
    total_categories,
    get_user_mybooks
)

def show():

    jumlah_buku = total_books()
    jumlah_kategori = total_categories()

    mybooks = get_user_mybooks(
        st.session_state.user_id
    )

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

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            with st.container(border=True):

                st.markdown("## 🔍 Search")

                st.write(
                    "Cari buku dengan cepat."
                )

                st.info(f"📚 {jumlah_buku} buku tersedia")

                if st.button(
                    "Cari Buku",
                    use_container_width=True,
                    key="home_search"
                ):

                    st.session_state.menu = "🔍 Search"
                    st.rerun()

        with col2:

            with st.container(border=True):

                st.markdown("## 📚 Katalog")

                st.write(
                    "Jelajahi seluruh koleksi ebook."
                )

                st.info(f"📖 {jumlah_kategori} kategori buku")

                if st.button(
                    "Buka Katalog",
                    use_container_width=True,
                    key="home_katalog"
                ):

                    st.session_state.menu = "📚 Katalog"
                    st.rerun()

        with col3:

            with st.container(border=True):

                st.markdown("## 📖 My Books")

                st.write(
                    "Semua buku favoritmu ada di sini."
                )

                st.info(f"⭐ {len(mybooks)} buku tersimpan")

                if st.button(
                    "Lihat Buku",
                    use_container_width=True,
                    key="home_mybooks"
                ):

                    st.session_state.menu = "📖 My Books"
                    st.rerun()

        with col4:

            with st.container(border=True):

                st.markdown("## 👤 Profil")

                st.write(
                    "Kelola akun Balance Library."
                )

                st.info(
                    f"👋 Halo, {st.session_state.user['Nama']}"
                )

                if st.button(
                    "Lihat Profil",
                    use_container_width=True,
                    key="home_profile"
                ):

                    st.session_state.menu = "👤 Profil"
                    st.rerun()