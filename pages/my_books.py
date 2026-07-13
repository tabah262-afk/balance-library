import streamlit as st
from database.database import (
    get_user_mybooks,
    get_book_by_id,
    delete_mybook
)

def show():

    st.title("📖 My Books")
    st.caption("Daftar buku yang telah kamu simpan.")

    mybooks = get_user_mybooks(
        st.session_state.user["ID"]
    )

    if len(mybooks) == 0:
        st.info("Belum ada buku yang disimpan.")
        return

    for item in mybooks:

        book = get_book_by_id(item["ID Buku"])

        if book is None:
            continue

        with st.container(border=True):

            col1, col2 = st.columns([1,4])

            with col1:

                if book["Cover"] != "-":
                    st.image(book["Cover"], width=120)
                else:
                    st.image(
                        "https://placehold.co/180x250?text=No+Cover",
                        width=120
                    )

            with col2:

                st.subheader(book["Judul"])

                st.write(f"👤 **Penulis :** {book['Penulis']}")
                st.write(f"🏢 **Penerbit :** {book['Penerbit']}")
                st.write(f"📚 **Kategori :** {book['Kategori']}")

                st.caption(book["Deskripsi"])

                c1, c2 = st.columns(2)

                with c1:

                    st.link_button(
                        "📖 Baca Buku",
                        book["Link PDF"]
                    )

                with c2:

                    if st.button(
                        "🗑 Hapus",
                        key=f"hapus_{book['ID Buku']}"
                    ):

                        hapus = delete_mybook(
                            st.session_state.user["ID"],
                            book["ID Buku"]
                        )

                        if hapus:
                            st.success("Buku berhasil dihapus.")
                            st.rerun()
                        else:
                            st.error("Gagal menghapus.")