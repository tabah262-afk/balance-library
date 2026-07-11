import streamlit as st

def show():

    st.sidebar.image("assets/logo.png", width=120)

    st.sidebar.markdown("## Balance Library")
    st.sidebar.caption("Smart Reading Starts Here")

    st.sidebar.divider()

    menu = st.sidebar.radio(
        "Menu",
        [
            "🏠 Home",
            "🔍 Search",
            "📚 Katalog",
            "📖 My Books",
            "👤 Profil"
        ]
    )

    st.sidebar.divider()

    st.sidebar.success("Versi 1.0")

    st.sidebar.caption("© 2026 Universitas Negeri Jakarta")

    return menu