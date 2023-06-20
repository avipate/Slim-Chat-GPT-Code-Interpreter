# Importing required libraries
import requests
import base64
import streamlit as st
import openai

URL = "https://horrible-mole-67.loc.lt"
headers = {'Bypass-Tunnel-Reminder': "go",
           'mode': 'no-cors'}


# Creating backend
def check_if_valid_backend(url):
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        return resp.status_code == 200
    except requests.exceptions.Timeout:
        return False


# Creating dalle function to get num of images
def call_dalle(url, text, num_images=1):
    data = {"text": text, "num_images": num_images}
    resp = requests.post(url + "/dalle", headers=headers, json=data)
    if resp.status_code == 200:
        return resp


# Show the image using streamlit
def create_and_show_images(text, num_images):
    valid = check_if_valid_backend(URL)
    if not valid:
        st.write("Backend Service is not Running")
    else:
        resp = call_dalle(URL, text, num_images)
        if resp is not None:
            for data in resp.json():
                img_data = base64.b64decode(data)   # To validate the image data
                st.image(img_data)

