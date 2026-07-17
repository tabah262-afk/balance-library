import streamlit as st

def show():

    st.sidebar.image("assets/logo.png", width=120)

    st.sidebar.markdown("## Balance Library")
    st.sidebar.caption("Smart Reading Starts Here")

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