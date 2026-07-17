import streamlit as st
from database.database import (
    add_user,
    login_user
)

def login_page():

    # Kolom kiri - tengah - kanan
    kiri, tengah, kanan = st.columns([1, 2, 1])

    with tengah:

        # Card Login
        with st.container(border=True):

            # Logo
            logo1, logo2, logo3 = st.columns([1,2,1])

            with logo2:
                st.image(
                    "assets/logo.png",
                    width=140
                )

            st.markdown(
                """
                <h2 style="text-align:center;">
                Balance Library
                </h2>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <p style="text-align:center;color:gray;">
                Smart Reading Starts Here
                </p>
                """,
                unsafe_allow_html=True
            )

            st.divider()

            email = st.text_input(
                "📧 Email"
            )

            password = st.text_input(
                "🔒 Password",
                type="password"
            )

            if st.button(
                "Login",
                use_container_width=True
            ):

                user = login_user(email, password)

                if user:

                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.user_id = user["ID"]

                    st.rerun()

                else:
                    st.error("Email atau Password salah.")

            st.divider()

            st.markdown(
                "<p style='text-align:center;'>Belum punya akun?</p>",
                unsafe_allow_html=True
            )

            if st.button(
                "Daftar Sekarang",
                use_container_width=True
            ):
                st.session_state.show_register = True
                st.rerun()

def register_page():

    st.title("📚 Balance Library")

    st.subheader("Sign Up")

    nama = st.text_input("Nama")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password",
        key="register_password"
    )

    konfirmasi = st.text_input(
        "Konfirmasi Password",
        type="password",
        key="register_konfirmasi"
    )

    if st.button("Daftar"):

        if nama == "" or email == "" or password == "":
            st.warning("Semua data wajib diisi.")

        elif password != konfirmasi:
            st.error("Konfirmasi password tidak sama.")

        else:

            berhasil = add_user(
                nama,
                email,
                password
            )

            if berhasil:

                st.success("Registrasi berhasil! Silakan login.")

            else:

                st.error("Email sudah terdaftar.")

    st.divider()

    if st.button("Kembali ke Login"):

        st.session_state.show_register = False

        st.rerun()