# Importing required libraries
import streamlit as st
from dalle import create_and_show_images

st.title("DALL-E Mini")

text = st.text_input("What should I Create ?")

num_images = st.slider("How Many Images?", 1, 6)

ok = st.button("GO!!")

if ok:
    create_and_show_images(text, num_images)
