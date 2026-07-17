import streamlit as st

from database.database import (
    total_books,
    total_categories,
    get_user_mybooks,
    search_books,
    latest_books
    )

def show():

    # ==========================
    # Ambil Data
    # ==========================

    jumlah_buku = total_books()
    jumlah_kategori = total_categories()

    mybooks = get_user_mybooks(
        st.session_state.user_id
    )

    latest = latest_books()

    # ==========================
    # HEADER
    # ==========================

    kiri, tengah, kanan = st.columns([1,2,1])

    with tengah:

        st.image(
            "assets/logo.png",
            width=180
        )

        st.markdown(
            f"""
            <h2 style='text-align:center;margin-bottom:0;'>
            Halo, {st.session_state.user["Nama"]} 👋
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style='text-align:center;color:gray;font-size:18px;'>
            Temukan koleksi ebook terbaikmu.
            </p>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ==========================
    # SEARCH
    # ==========================

    kiri, tengah, kanan = st.columns([1,2,1])

    with tengah:

        st.subheader("🔍 Cari Buku")

        keyword = st.text_input(
            "",
            placeholder="Cari judul buku..."
        )

        if keyword:

            hasil = search_books(keyword)

            if hasil:

                st.write("### Hasil Pencarian")

                for buku in hasil:

                    with st.container(border=True):

                        st.markdown(f"### 📘 {buku['Judul']}")

                        st.caption(
                            f"👤 {buku['Penulis']}"
                        )

            else:

                st.warning(
                    "😕 Buku tidak ditemukan."
                )

    st.divider()

    # ==========================
    # QUICK STATISTICS
    # ==========================

    kiri, tengah, kanan = st.columns([1,2,1])

    with tengah:

        st.subheader("📊 Quick Statistics")

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown(
                    "<h3 style='text-align:center;'>📚</h3>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<h2 style='text-align:center;'>{jumlah_buku}</h2>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    "<p style='text-align:center;'>Total Buku</p>",
                    unsafe_allow_html=True
                )

        with col2:

            with st.container(border=True):

                st.markdown(
                    "<h3 style='text-align:center;'>📂</h3>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<h2 style='text-align:center;'>{jumlah_kategori}</h2>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    "<p style='text-align:center;'>Kategori</p>",
                    unsafe_allow_html=True
                )

    st.divider()

    # ==========================
    # BUKU TERBARU
    # ==========================

    kiri, tengah, kanan = st.columns([1,2,1])

    with tengah:

        st.subheader("✨ Buku Terbaru")

        for book in latest:

            with st.container(border=True):

                col1, col2 = st.columns([1,4])

                with col1:

                    if book["Cover"] != "-":
                        st.image(
                            book["Cover"],
                            width=80
                        )
                    else:
                        st.image(
                            "https://placehold.co/120x180?text=No+Cover",
                            width=80
                        )

                with col2:

                    st.markdown(
                        f"### {book['Judul']}"
                    )

                    st.caption(
                        f"👤 {book['Penulis']}"
                    )

                    st.write(
                        f"📂 {book['Kategori']}"
                    )

                    st.link_button(
                        "📖 Baca Buku",
                        book["Link PDF"],
                        use_container_width=True
                )
                    
    st.divider()

    # ==========================
    # MENU CEPAT
    # ==========================

    kiri, tengah, kanan = st.columns([1,2,1])

    with tengah:

        st.subheader("⚡ Menu Cepat")

        atas1, atas2 = st.columns(2)

        with atas1:

            if st.button(
                "📚 Katalog",
                use_container_width=True,
                key="menu_katalog"
            ):

                st.session_state.menu = "📚 Katalog"
                st.rerun()

        with atas2:

            if st.button(
                "📖 My Books",
                use_container_width=True,
                key="menu_mybooks"
            ):

                st.session_state.menu = "📖 My Books"
                st.rerun()

        bawah1, bawah2 = st.columns(2)

        with bawah1:

            if st.button(
                "👤 Profil",
                use_container_width=True,
                key="menu_profil"
            ):

                st.session_state.menu = "👤 Profil"
                st.rerun()

        with bawah2:

            if st.button(
                "🚪 Log Out",
                use_container_width=True,
                key="menu_logout"
            ):

                st.session_state.logged_in = False
                st.session_state.menu = "🏠 Home"

                st.session_state.pop("user", None)
                st.session_state.pop("user_id", None)

                st.rerun()