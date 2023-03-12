import streamlit as st
import pandas as pd

st.title('Aplikasi Presensi Siswa dengan Streamlit')

# Mengupload file CSV dengan daftar nama siswa
uploaded_file = st.file_uploader('Upload daftar nama siswa (CSV)', type='csv')

# Jika file berhasil diupload
if uploaded_file is not None:
    # Membaca file CSV ke dalam DataFrame
    df = pd.read_csv(uploaded_file)

    # Menampilkan DataFrame
    st.write('Daftar nama siswa:', df)

    # Menggunakan input tanggal untuk melakukan presensi
    tanggal = st.date_input('Pilih tanggal')

    # Membuat kolom baru dalam DataFrame dengan nama tanggal yang dipilih
    df[str(tanggal)] = ''

    # Memasukkan status presensi siswa menggunakan checkbox
    for index, row in df.iterrows():
        nama_siswa = row['Nama Siswa']
        hadir = st.checkbox(nama_siswa + ' (Hadir)')
        if hadir:
            df.loc[index, str(tanggal)] = 'Hadir'

    # Menampilkan DataFrame setelah presensi
    st.write('Daftar nama siswa setelah presensi:', df)
