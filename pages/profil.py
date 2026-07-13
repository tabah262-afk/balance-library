import streamlit as st


def show():

    st.title("👤 Profil")

    user = st.session_state.user

    st.subheader(user["Nama"])

    st.write(f"📧 **Email :** {user['Email']}")
    st.write(f"🛡️ **Role :** {user['Role']}")
    st.write(f"📅 **Tanggal Daftar :** {user['Tanggal Daftar']}")

    st.divider()

    if st.button("🚪 Logout", type="primary"):

        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.show_register = False

        st.rerun()