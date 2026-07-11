import streamlit as st

from components.navbar import show as show_navbar
from pages.home import show as show_home

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

menu = show_navbar()

if menu == "🏠 Home":
    show_home()