import streamlit as st

def show():

    # ==========================
    # LOGO
    # ==========================

    kiri, tengah, kanan = st.sidebar.columns([1,3,1])

    with tengah:
        st.image(
            "assets/logo.png",
            width=160
        )

    st.sidebar.markdown("")

    st.sidebar.markdown(
        f"""
        <h4 style="text-align:center;">
            👋 Halo, {st.session_state.user["Nama"]}
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.divider()

    # ==========================
    # MENU
    # ==========================

    if "menu" not in st.session_state:
        st.session_state.menu = "🏠 Home"


    def menu_button(icon, title):

        aktif = st.session_state.menu == f"{icon} {title}"

        if aktif:
            label = f"🟦 {icon} {title}"
        else:
            label = f"{icon} {title}"

        if st.sidebar.button(
            label,
            use_container_width=True
        ):
            st.session_state.menu = f"{icon} {title}"
            st.rerun()


    menu_button("🏠", "Home")
    menu_button("🔍", "Search")
    menu_button("📚", "Katalog")
    menu_button("📖", "My Books")
    menu_button("👤", "Profil")

    menu = st.session_state.menu

    st.sidebar.divider()

    # ==========================
    # LOG OUT
    # ==========================

    if st.sidebar.button(
        "🚪 Log Out",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.menu = "🏠 Home"

        st.session_state.pop("user", None)
        st.session_state.pop("user_id", None)

        st.rerun()

    st.sidebar.divider()

    st.sidebar.markdown(
        """
        <div style="
            text-align:center;
            color:#94A3B8;
            font-size:12px;
            line-height:1.5;
        ">
            Version 1.0<br>
            © 2026 Universitas Negeri Jakarta
        </div>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.menu