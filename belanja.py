import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_invoice(items, total):
    # Buat file PDF baru
    c = canvas.Canvas("invoice.pdf", pagesize=letter)

    # Tambahkan informasi header
    c.setFont('Helvetica', 14)
    c.drawString(50, 750, 'INVOICE')

    # Tambahkan daftar item
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, 700, 'Item')
    c.drawString(250, 700, 'Harga')

    c.setFont('Helvetica', 12)
    y = 670
    for item in items:
        c.drawString(50, y, item['name'])
        c.drawString(250, y, str(item['price']))
        y -= 20

    # Tambahkan total belanja
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, y-20, 'Total')
    c.drawString(250, y-20, str(total))

    c.save()

def main():
    st.title("Aplikasi Belanja")

    items = []
    total = 0

    # Tampilkan form untuk memasukkan item belanja
    name = st.text_input("Nama item:")
    price = st.number_input("Harga item:", value=0)
    if st.button("Tambahkan item"):
        items.append({"name": name, "price": price})
        total += price

    # Tampilkan daftar item belanja
    st.write("Daftar Item:")
    for item in items:
        st.write(f"{item['name']}: {item['price']}")

    # Tampilkan total belanja
    st.write(f"Total: {total}")

    # Buat invoice jika ada item belanja
    if items:
        if st.button("Buat Invoice"):
            create_invoice(items, total)
            st.write("Invoice berhasil dibuat!")
            st.write("Silahkan cek file invoice.pdf")

if __name__ == "__main__":
    main()
