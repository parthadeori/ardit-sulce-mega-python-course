import requests
import streamlit as st 

# Prepare API Key and API URL
api_key = "F2OUneFq5aianeWrSHEShavhFddGAUamhQsqmrgR"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content) 

st.title(title)
st.image(image_filepath)
st.write(explanation)