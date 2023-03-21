import streamlit as st

def intro():
    import streamlit as st

    

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
            forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
            Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def kasir_sederhana():
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

def kasir_sederhana1():
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

    # Creating a drop-down menu to select items
    menu_item = st.selectbox("Silahkan pilih menu yang diinginkan:", list(items.keys()))

    # Creating a slider to select the quantity of the items
    quantity = st.slider("Jumlah:", 1, 10, 1)

    # Adding the selected item and quantity to the cart dictionary
    if st.button("Tambahkan ke keranjang"):
        if menu_item in cart.keys():
            cart[menu_item] += quantity
        else:
            cart[menu_item] = quantity
        total_price += items[menu_item] * quantity

    # Displaying the cart and the total price
    if len(cart) > 0:
        st.write("Pesanan Anda:")
        for item in cart:
            st.write("- " + item + ": " + str(cart[item]))
        st.write("Total harga: Rp. " + str(total_price))
    else:
        st.write("Keranjang belanja masih kosong.")

    # Creating a checkout button
    if st.button("Bayar"):
        st.write("Terima kasih telah memesan. Silahkan tunggu pesanan Anda.")
        
def kasir_sederhana2():
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

    # Creating a drop-down menu to select items
    menu_item = st.selectbox("Silahkan pilih menu yang diinginkan:", list(items.keys()))

    # Creating a slider to select the quantity of the items
    quantity = st.slider("Jumlah:", 1, 10, 1)

    # Adding the selected item and quantity to the cart dictionary
    if st.button("Tambahkan ke keranjang"):
        if menu_item in cart.keys():
            cart[menu_item] += quantity
        else:
            cart[menu_item] = quantity
        total_price += items[menu_item] * quantity

    # Displaying the cart and the total price
    if len(cart) > 0:
        st.write("Keranjang belanja:")
        for item in cart:
            st.write("- " + item + ": " + str(cart[item]) + " x " + "Rp. " + str(items[item]) + " = Rp. " + str(cart[item] * items[item]))
        st.write("Subtotal: Rp. " + str(total_price))
    else:
        st.write("Keranjang belanja masih kosong.")

    # Creating a checkout button
    if st.button("Bayar"):
        st.write("Total harga: Rp. " + str(total_price))
        st.write("Terima kasih telah memesan. Silahkan tunggu pesanan Anda.")

def kasir_sederhana3():
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

    
page_names_to_funcs = {
    "—": intro,
    "Kasir Sederhana": kasir_sederhana,
    "Kasir Sederhana 1": kasir_sederhana1,
    "kasir sederhana 2": kasir_sederhana2,
    "kasir sederhana dengan multi select": kasir_sederhana3,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()


