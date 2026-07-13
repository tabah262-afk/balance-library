import streamlit as st
from database.database import (
    add_user,
    login_user
)

def login_page():

    st.title("📚 Balance Library")

    st.subheader("Sign In")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if email == "" or password == "":
            st.warning("Email dan password wajib diisi.")

        else:

            user = login_user(
                email,
                password
            )

            if user is None:

                st.error(
                    "Email atau password salah.\n\n"
                    "Jika belum memiliki akun, silakan Sign Up terlebih dahulu."
                )

            else:

                st.session_state.logged_in = True

                st.session_state.user = user

                st.success("Login berhasil!")

                st.rerun()

    st.divider()

    st.write("Belum punya akun?")

    if st.button("Sign Up"):

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