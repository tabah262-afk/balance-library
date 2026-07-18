import streamlit as st

def show():

    # ==========================
    # LOGO
    # ==========================

    kiri, tengah, kanan = st.sidebar.columns([1,2,1])

    with tengah:
        st.image(
            "assets/logo.png",
            use_container_width=True
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

    if "menu" not in st.session_state:
        st.session_state.menu = "🏠 Home"

    menu_list = [
        "🏠 Home",
        "🔍 Search",
        "📚 Katalog",
        "📖 My Books",
        "👤 Profil"
    ]

    menu = st.sidebar.radio(
        "Menu",
        menu_list,
        index=menu_list.index(st.session_state.menu)
    )

    st.session_state.menu = menu

    st.sidebar.divider()

    st.sidebar.success("Versi 1.0")

    st.sidebar.caption("© 2026 Universitas Negeri Jakarta")

    return menu