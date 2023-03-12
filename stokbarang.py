import streamlit as st
import pandas as pd

st.title('Aplikasi Manajemen Stok Barang dengan Streamlit')

# Mengupload file CSV dengan daftar barang
uploaded_file = st.file_uploader('Upload daftar barang (CSV)', type='csv')

# Jika file berhasil diupload
if uploaded_file is not None:
    # Membaca file CSV ke dalam DataFrame
    df = pd.read_csv(uploaded_file)

    # Menampilkan DataFrame
    st.write('Daftar barang:', df)

    # Menampilkan dropdown untuk memilih barang yang ingin diubah stoknya
    nama_barang = st.selectbox('Pilih nama barang:', df['Nama Barang'].unique())

    # Menampilkan form untuk mengubah stok barang
    with st.form('form_ubah_stok'):
        st.write('Ubah stok barang ', nama_barang)
        st.number_input('Stok masuk', key='stok_masuk')
        st.number_input('Stok keluar', key='stok_keluar')
        submit_button = st.form_submit_button(label='Simpan')

        # Jika tombol simpan ditekan
        if submit_button:
            # Mencari indeks baris yang mengandung nama barang yang dipilih
            index = df.index[df['Nama Barang'] == nama_barang].tolist()[0]

            # Mengubah nilai stok barang di DataFrame
            stok_masuk = st.session_state['stok_masuk']
            stok_keluar = st.session_state['stok_keluar']
            stok_sekarang = df.loc[index, 'Stok'] + stok_masuk - stok_keluar
            df.loc[index, 'Stok'] = stok_sekarang

            # Menampilkan DataFrame setelah stok barang diubah
            st.write('Daftar barang setelah stok barang diubah:', df)
