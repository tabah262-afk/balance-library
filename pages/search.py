import streamlit as st
from database.database import (
    get_books,
    save_mybook
)

def show():

    st.title("🔍 Search Buku")
    st.caption("Cari buku berdasarkan judul, penulis, penerbit, atau kata kunci.")

    keyword = st.text_input(
        "Cari Buku",
        placeholder="Contoh : auditing, kieso, pajak..."
    )

    books = get_books()

    if keyword == "":
        st.info("Masukkan kata kunci untuk mulai mencari.")
        return

    keyword = keyword.lower()

    hasil = []

    for book in books:

        teks = (
            str(book["Judul"]) + " " +
            str(book["Penulis"]) + " " +
            str(book["Penerbit"]) + " " +
            str(book["Kategori"]) + " " +
            str(book["Kata Kunci"]) + " " +
            str(book["Deskripsi"])
        ).lower()

        if keyword in teks:
            hasil.append(book)

    st.write(f"📚 Ditemukan **{len(hasil)}** buku")

    st.divider()

    if len(hasil) == 0:
        st.warning("Tidak ada buku yang ditemukan.")
        return

    for book in hasil:

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

                with c2:
                    st.link_button(
                        "📖 Baca Buku",
                        book["Link PDF"]
                    )