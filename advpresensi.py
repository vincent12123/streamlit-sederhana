import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='Aplikasi Presensi Siswa dengan Streamlit')

st.title('Aplikasi Presensi Siswa dengan Streamlit')

# Mengupload file CSV dengan daftar nama siswa
uploaded_file = st.file_uploader('Upload daftar nama siswa (CSV)', type='csv')

# Jika file berhasil diupload
if uploaded_file is not None:
    # Membaca file CSV ke dalam DataFrame
    df = pd.read_csv(uploaded_file)

    # Menampilkan DataFrame
    st.write('Daftar nama siswa:', df)

    # Membuat kolom baru dalam DataFrame dengan nama tanggal yang dipilih
    tanggal = st.date_input('Pilih tanggal')

    # Mengecek apakah kolom presensi untuk tanggal yang dipilih sudah ada di DataFrame
    if str(tanggal) not in df.columns:
        df[str(tanggal)] = ''

    # Membuat kolom baru dalam DataFrame untuk menghitung jumlah siswa hadir di setiap tanggal
    df['Jumlah Hadir'] = df.iloc[:, 2:].apply(lambda x: x.str.contains('Hadir').sum(), axis=1)

    # Menampilkan jumlah siswa hadir untuk setiap tanggal
    st.write('Jumlah siswa hadir untuk setiap tanggal:', df.groupby(str(tanggal)).sum()[['Jumlah Hadir']])

    # Membuat pilihan filter berdasarkan tanggal
    pilihan_tanggal = st.selectbox('Filter berdasarkan tanggal:', sorted(df.columns[2:-1], reverse=True))

    # Menampilkan DataFrame setelah presensi
    st.write('Daftar nama siswa setelah presensi:', df[df[pilihan_tanggal] != ''].reset_index(drop=True))

    # Membuat kolom baru dalam DataFrame untuk menghitung jumlah siswa hadir di setiap kelas
    df['Jumlah Hadir Kelas'] = df.iloc[:, 2:-1].apply(lambda x: x.str.contains('Hadir').sum(), axis=0)

    # Menampilkan jumlah siswa hadir untuk setiap kelas
    st.write('Jumlah siswa hadir untuk setiap kelas:', df.groupby('Kelas').sum()[['Jumlah Hadir Kelas']])

    # Membuat input untuk pencarian nama siswa
    cari_siswa = st.text_input('Cari nama siswa')

    # Menampilkan DataFrame setelah presensi dengan filter pencarian nama siswa
    st.write('Daftar nama siswa setelah presensi dengan filter pencarian nama siswa:', df[df['Nama Siswa'].str.contains(cari_siswa, case=False)].reset_index(drop=True))

    # Memasukkan status presensi siswa menggunakan checkbox
    for index, row in df.iterrows():
        nama_siswa = row['Nama Siswa']
        hadir = st.checkbox(nama_siswa + ' (Hadir)', key=index)
        if hadir:
            df.loc[index, str(tanggal)] = 'Hadir'

    # Menampilkan DataFrame setelah presensi
    st.write('Daftar nama siswa setelah presensi:', df)
