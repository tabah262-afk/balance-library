import streamlit as st

# IMPORT NAVBAR
from components.navbar import show as show_navbar

# IMPORT HALAMAN
from pages.home import show as show_home
from pages.search import show as show_search
from pages.katalog import show as show_katalog
from pages.my_books import show as show_mybooks
from pages.profil import show as show_profil

# ==========================
# Konfigurasi Halaman
# ==========================
st.set_page_config(
    page_title="Balance Library",
    page_icon="📚",
    layout="wide"
)

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