import streamlit as st
from streamlit_folium import folium_static
import folium
m = folium.Map(location=[0.03330359995287797, 111.46270391314616], zoom_start=17)
tooltip = 'SMK Karya Bangsa Sintang'
folium.Marker([0.03330359995287797, 111.46270391314616], popup='<i>SMK Karya Bangsa Sintang</i>', tooltip=tooltip).add_to(m)
folium_static(m)
