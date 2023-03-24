import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv('data_siswa.csv')

# Define login function
def login():
    st.sidebar.title('Login')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')
    if st.sidebar.button('Login'):
        if username == 'admin' and password == '12345':
            return True
        else:
            st.sidebar.error('Invalid username or password')
    else:
        return False

# Main function
def main():
    # Check login
    if login():
        # Hide login form
        st.sidebar.empty()

        # Sidebar
        st.sidebar.title('Filter Data')
        kelas = st.sidebar.selectbox('Kelas', data['Kelas'].unique())
        tanggal = st.sidebar.date_input('Tanggal', pd.to_datetime('today'))

        # Filter data
        data_filtered = data[(data['Kelas'] == kelas) & (data['Tanggal'] == tanggal)]

        # Display data
        st.write('### Daftar Absensi Siswa')
        st.write(data_filtered)

# Run app
if __name__ == '__main__':
    main()
