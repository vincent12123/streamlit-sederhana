import streamlit as st

st.title('Aplikasi Input Data dengan Streamlit')

# Memasukkan data menggunakan st.text_input
nama = st.text_input('Masukkan Nama')
alamat = st.text_input('Masukkan Alamat')

# Memasukkan data menggunakan st.slider
usia = st.slider('Masukkan Usia', 0, 100, 25)

# Memasukkan data menggunakan st.number_input
gaji = st.number_input('Masukkan Gaji', min_value=0, max_value=1000000000, step=1000000)

# Menampilkan data yang dimasukkan
st.write('Data yang dimasukkan:')
st.write('Nama:', nama)
st.write('Alamat:', alamat)
st.write('Usia:', usia)
st.write('Gaji:', gaji)
