import streamlit as st

st.title("Program Kasir Sederhana")

menu = {"Nasi Goreng": 15000, "Mie Ayam": 12000, "Bakso": 10000, "Sate": 20000}

order = []
total_harga = 0

option = st.selectbox(
    'Silahkan pilih menu yang diinginkan:',
    list(menu.keys()))

order.append(option)
total_harga += menu[option]

st.write("Pesanan Anda:")
for item in order:
    st.write("- " + item)
st.write("Total harga: Rp. " + str(total_harga))

if st.button("Pesan"):
    st.write("Terima kasih telah memesan. Silahkan tunggu pesanan Anda.")
