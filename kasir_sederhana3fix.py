import streamlit as st

# List of available items
items = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Bakso": 10000,
    "Sate Ayam": 20000,
    "Es Teh Manis": 5000,
    "Es Jeruk": 7000,
    "Air Mineral": 3000
}

# Initializing variables
cart = {}
total_price = 0

# Title of the web app
st.title("Program Kasir Restoran")

# Creating a multiselect to select items and sliders for each selected item
selected_items = st.multiselect("Silahkan pilih menu yang diinginkan:", list(items.keys()))
quantities = {}
for item in selected_items:
    quantities[item] = st.slider(f"Jumlah {item}:", 1, 10, 1)

# Adding the selected item and quantity to the cart dictionary
if st.button("Bayar"):
    for item in quantities:
        if quantities[item] > 0:
            cart[item] = quantities[item]
            total_price += items[item] * quantities[item]

# Displaying the cart and the total price
if len(cart) > 0:
    st.write("Keranjang belanja:")
    for item in cart:
        st.write("- " + item + ": " + str(cart[item]) + " x " + "Rp. " + str(items[item]) + " = Rp. " + str(cart[item] * items[item]))
    st.write("Subtotal: Rp. " + str(total_price))
    st.write("Terima kasih, total pembayaran anda adalah Rp. " +str(total_price), " Silahkan tunggu pesanan Anda")
else:
    st.write("Keranjang belanja masih kosong.")
