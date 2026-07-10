import streamlit as st

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
# SIDEBAR
# ==========================

with st.sidebar:

    st.image("assets/logo.png", width=120)

    st.markdown("## Balance Library")
    st.caption("Smart Reading Starts Here")

    st.divider()

    st.write("🏠 Home")
    st.write("📚 Katalog Buku")
    st.write("❤️ Favorit")
    st.write("👤 Profil")

    st.divider()

    st.success("Versi 1.0")
    st.caption("© 2026 Universitas Negeri Jakarta")

# ==========================
# Landing Page
# ==========================

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("assets/logo.png", width=180)

st.title("Balance Library")

st.subheader("Perpustakaan Digital Berbasis Android")

st.markdown("""
### Selamat Datang 👋

**Balance Library** adalah aplikasi perpustakaan digital yang membantu
pengguna menemukan, membaca, dan mengelola koleksi buku dengan mudah.

""")

st.divider()

st.divider()

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("## 📚")
        st.subheader("Jelajahi Buku")
        st.caption("Lihat seluruh koleksi buku digital.")
        st.button("Buka", key="buku")

with col2:
    with st.container(border=True):
        st.markdown("## 📖")
        st.subheader("Buku Saya")
        st.caption("Lihat riwayat peminjaman buku.")
        st.button("Buka", key="bukusaya")

st.write("")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown("## 🔍")
        st.subheader("Cari Buku")
        st.caption("Cari buku berdasarkan judul atau penulis.")
        st.button("Cari", key="cari")

with col4:
    with st.container(border=True):
        st.markdown("## 👤")
        st.subheader("Akun Saya")
        st.caption("Masuk dan kelola akun pengguna.")
        st.button("Login", key="login")