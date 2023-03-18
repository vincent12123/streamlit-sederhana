import streamlit as st
import pandas as pd
import mysql.connector

# Membuat koneksi ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ppdbonline"
)

# Membuat cursor
mycursor = mydb.cursor()

# Query untuk mengambil data dari tabel
sql = "SELECT nama_lengkap, jk, alamat_siswa, nama_ayah, no_hp_siswa, no_hp_ortu FROM tbl_siswa"
mycursor.execute(sql)

# Membuat dataframe dari hasil query
df = pd.DataFrame(mycursor.fetchall(), columns=["Nama Lengkap", "Jenis Kelamin", "Alamat Siswa", "Nama Ayah", "Nomor HP Siswa", "Nomor HP Orang Tua"])

# Menghilangkan baris kosong
df = df.dropna()
# Menampilkan dataframe sebagai tabel
st.table(df)
