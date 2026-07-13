import os
from datetime import datetime
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

if os.path.exists("database/credentials.json"):
    creds = Credentials.from_service_account_file(
        "database/credentials.json",
        scopes=SCOPES
    )
else:
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )


client = gspread.authorize(creds)

# ==========================
# Buka Spreadsheet
# ==========================

spreadsheet = client.open("Balance Library Database")

# ==========================
# Ambil Sheet
# ==========================

users_sheet = spreadsheet.worksheet("Users")
books_sheet = spreadsheet.worksheet("Books")
categories_sheet = spreadsheet.worksheet("Categories")
mybooks_sheet = spreadsheet.worksheet("My Books")

# ==========================
# Functions
# ==========================

def get_users():
    return users_sheet.get_all_records()

def get_books():
    return books_sheet.get_all_records()

def get_categories():
    return categories_sheet.get_all_records()

def get_mybooks():
    return mybooks_sheet.get_all_records()

def save_mybook(id_user, id_buku):

    data = mybooks_sheet.get_all_records()

    # Cek apakah buku sudah pernah disimpan
    for row in data:
        if row["ID User"] == id_user and row["ID Buku"] == id_buku:
            return False

    new_id = len(data) + 1

    mybooks_sheet.append_row([
        new_id,
        id_user,
        id_buku,
        "-",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ])

    return True

def get_user_mybooks(id_user):

    data = mybooks_sheet.get_all_records()

    hasil = []

    for row in data:
        if row["ID User"] == id_user:
            hasil.append(row)

    return hasil

def get_book_by_id(id_buku):

    books = books_sheet.get_all_records()

    for book in books:
        if book["ID Buku"] == id_buku:
            return book

    return None

def delete_mybook(id_user, id_buku):

    data = mybooks_sheet.get_all_records()

    for i, row in enumerate(data, start=2):

        if row["ID User"] == id_user and row["ID Buku"] == id_buku:

            mybooks_sheet.delete_rows(i)

            return True

    return False

# ==========================
# Tambah User Baru
# ==========================

def add_user(nama, email, password):

    users = users_sheet.get_all_records()

    # Cek apakah email sudah digunakan
    for user in users:
        if user["Email"].lower() == email.lower():
            return False

    # Membuat ID baru
    new_id = f"U{len(users)+1:03d}"

    users_sheet.append_row([
        new_id,
        nama,
        email,
        password,
        "User",
        "Aktif",
        datetime.now().strftime("%d/%m/%Y")
    ])

    return True

def login_user(email, password):

    users = users_sheet.get_all_records()

    for user in users:

        if (
            user["Email"].lower() == email.lower()
            and user["Password"] == password
        ):
            return user

    return None