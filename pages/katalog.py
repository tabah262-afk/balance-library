import streamlit as st
from database.database import (
    get_books,
    get_categories,
    save_mybook
)


def show():

    st.title("📚 Katalog Buku")
    st.caption("Temukan berbagai koleksi buku digital.")

    books = get_books()
    categories = get_categories()

    # ==========================
    # Dropdown kategori
    # ==========================

    pilihan = ["Semua"]

    for kategori in categories:
        pilihan.append(kategori["Nama Kategori"])

    selected = st.selectbox(
        "Kategori",
        pilihan
    )

    st.divider()

    # ==========================
    # Tampilkan Buku
    # ==========================

    ditemukan = False

    for book in books:

        if selected != "Semua":
            if book["Kategori"] != selected:
                continue

        ditemukan = True

        with st.container(border=True):

            col1, col2 = st.columns([1,4])

            with col1:

                if book["Cover"] != "-":
                    st.image(book["Cover"], width=200)
                else:
                    st.image(
                        "https://placehold.co/180x250?text=No+Cover",
                        width=120
                    )

            with col2:

                st.subheader(book["Judul"])

                st.write(f"👤 **Penulis :** {book['Penulis']}")
                st.write(f"🏢 **Penerbit :** {book['Penerbit']}")
                st.write(f"📅 **Tahun :** {book['Tahun']}")
                st.write(f"📚 **Kategori :** {book['Kategori']}")
                st.write(f"📄 **Halaman :** {book['Halaman']}")

                st.caption(book["Deskripsi"])

                tombol1, tombol2 = st.columns(2)

                with tombol1:

                    if st.button(
                        "🔖 Simpan",
                        key=f"simpan_{book['ID Buku']}"
                    ):
                        berhasil = save_mybook(
                            st.session_state.user["ID"], 
                            book["ID Buku"]
                        )

                        if berhasil:
                            st.success("Buku berhasil disimpan.")
                        else:
                            st.warning("Buku sudah ada di My Books.")

                with tombol2:

                    st.link_button(
                        "📖 Baca Buku",
                        book["Link PDF"]
                    )

    if not ditemukan:
        st.warning("Belum ada buku pada kategori ini.")