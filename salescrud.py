import streamlit as st
import pandas as pd
import sqlite3

def create_data():
    # Get input from user
    product = st.text_input('Enter product name')
    price = st.number_input('Enter price')

    # Insert data into database
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute('INSERT INTO sales (product, price) VALUES (?, ?)', (product, price))
    conn.commit()
    conn.close()

def read_data():
    # Retrieve data from database
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sales')
    data = c.fetchall()
    conn.close()

    # Display data in a table
    df = pd.DataFrame(data, columns=['ID', 'Product', 'Price'])
    st.write(df)

def update_data():
    # Get input from user
    id = st.number_input('Enter ID of sale to update')
    product = st.text_input('Enter new product name')
    price = st.number_input('Enter new price')

    # Update data in database
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute('UPDATE sales SET product=?, price=? WHERE id=?', (product, price, id))
    conn.commit()
    conn.close()

def delete_data():
    # Get input from user
    id = st.number_input('Enter ID of sale to delete')

    # Delete data from database
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute('DELETE FROM sales WHERE id=?', (id,))
    conn.commit()
    conn.close()

# Create Streamlit app
st.title('Sales CRUD App')

menu = ['Create', 'Read', 'Update', 'Delete']
choice = st.sidebar.selectbox('Select operation', menu)

if choice == 'Create':
    create_data()
elif choice == 'Read':
    read_data()
elif choice == 'Update':
    update_data()
elif choice == 'Delete':
    delete_data()
