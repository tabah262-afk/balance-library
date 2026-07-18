import streamlit as st

# IMPORT NAVBAR
from components.navbar import show as show_navbar

# IMPORT HALAMAN
from pages.home import show as show_home
from pages.search import show as show_search
from pages.katalog import show as show_katalog
from pages.my_books import show as show_mybooks
from pages.profil import show as show_profil

# IMPORT AUTH
from utils.auth import (
    login_page,
    register_page
)   

# ==========================
# Konfigurasi Halaman
# ==========================
st.set_page_config(
    page_title="Balance Library",
    page_icon="assets/logo.png",
    layout="wide"
)

# ==========================
# Session Login
# ==========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "show_register" not in st.session_state:
    st.session_state.show_register = False

# ==========================
# Custom CSS
# ==========================
st.markdown("""
<style>

/* Background */
.stApp{
    background-color:#F8FAFC;
}

/* Judul */
h1{
    color:#1E3A8A;
}

/* Subjudul */
h2,h3{
    color:#2563EB;
}

/* Tombol */
.stButton>button{
    background-color:#1E3A8A;
    color:white;
    border-radius:10px;
    border:none;
    padding:10px 25px;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#3B82F6;
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#EAF2FF;
}

/* ==========================
   Menu Sidebar
========================== */

section[data-testid="stSidebar"] [data-baseweb="radio"] label{
    border-radius:10px;
    padding:8px 12px;
    margin-bottom:6px;
    transition:0.2s;
}

/* Hover menu */
section[data-testid="stSidebar"] [data-baseweb="radio"] label:hover{
    background-color:#D6E4FF;
}

/* Menu aktif */
section[data-testid="stSidebar"] [data-baseweb="radio"] label:has(input:checked){
    background-color:#BFDBFE;
    color:#1E3A8A;
    font-weight:bold;
}            

/* Hilangkan menu bawaan */
[data-testid="stSidebarNav"]{
    display:none;
}

/* Garis pembatas */
hr{
    border:1px solid #D6E4FF;
}

/* Caption */
.stCaption{
    color:#64748B;
}

/* Info Box */
div[data-testid="stAlert"]{
    border-radius:12px;
}
                        
</style>
""", unsafe_allow_html=True)

# ==========================
# Login Check
# ==========================

if not st.session_state.logged_in:

    if st.session_state.show_register:
        register_page()
    else:
        login_page()

    st.stop()

# ==========================
# NAVBAR
# ==========================

menu = show_navbar()

# ==========================
# ROUTING HALAMAN
# ==========================

if menu == "🏠 Home":
    show_home()

elif menu == "🔍 Search":
    show_search()

elif menu == "📚 Katalog":
    show_katalog()

elif menu == "📖 My Books":
    show_mybooks()

elif menu == "👤 Profil":
    show_profil()