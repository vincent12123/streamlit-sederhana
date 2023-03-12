import streamlit as st
import pandas as pd
import sqlite3

st.title('Aplikasi Manajemen Stok Barang dengan Sqllite')
# Membuat koneksi ke database SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Membuat tabel barang jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS barang
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT,
                stok INTEGER)''')



# Membaca data dari tabel barang ke dalam DataFrame
df = pd.read_sql_query("SELECT * FROM barang", conn, index_col='id')

nama = df['nama'].tolist()
# Menampilkan DataFrame
st.write('Daftar barang:', df)

# Menambahkan input untuk nama barang, stok masuk, dan stok keluar
nama_barang = st.selectbox('Pilih Nama barang:',nama)
stok_masuk = st.number_input('Stok masuk:', min_value=0)
stok_keluar = st.number_input('Stok keluar:', min_value=0)

# Menampilkan tombol simpan
submit_button = st.button('Simpan')

# Jika tombol simpan ditekan
if submit_button:
    # Mencari indeks baris yang mengandung nama barang yang dipilih
    index = df.index[df['nama'] == nama_barang].tolist()[0]

    # Mengubah nilai stok barang di DataFrame
    stok_sekarang = df.loc[index, 'stok'] + stok_masuk - stok_keluar
    df.loc[index, 'stok'] = stok_sekarang

    # Menampilkan DataFrame setelah stok barang diubah
    st.write('Daftar barang setelah stok barang diubah:', df)

    # Menyimpan DataFrame ke tabel barang dalam database SQLite
    for index, row in df.iterrows():
        cursor.execute("UPDATE barang SET stok = ? WHERE id = ?", (row['stok'], index))
    conn.commit()
    st.success('Data berhasil disimpan dalam tabel barang')

# Menutup koneksi ke database SQLite
conn.close()
