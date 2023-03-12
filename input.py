import streamlit as st

st.title('Aplikasi Kalkulator dengan Streamlit')

# Memasukkan data menggunakan st.number_input
a = st.number_input('Masukkan angka pertama')
b = st.number_input('Masukkan angka kedua')

# Menambahkan tombol untuk menjalankan kalkulator
tombol = st.button('Hitung')

# Jika tombol di klik
if tombol:
    # Menghitung hasil penjumlahan
    hasil = a + b

    # Menampilkan hasil
    st.write('Hasil penjumlahan:', hasil)
