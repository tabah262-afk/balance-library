import os
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