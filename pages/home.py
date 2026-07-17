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

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button(
                "📚 Jelajahi",
                use_container_width=True,
                key="home_katalog"
            ):
                st.session_state.menu = "📚 Katalog"
                st.rerun()

        with col2:
            if st.button(
                "❤️ Lihat",
                use_container_width=True,
                key="home_mybooks"
            ):
                st.session_state.menu = "📖 My Books"
                st.rerun()

        with col3:
            if st.button(
                "🔍 Cari Buku",
                use_container_width=True,
                key="home_search"
            ):
                st.session_state.menu = "🔍 Search"
                st.rerun()

        with col4:
            if st.button(
                "👤 Profil",
                use_container_width=True,
                key="home_profil"
            ):
                st.session_state.menu = "👤 Profil"
                st.rerun()