import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title("Streamlit App")
st.write("Upload an image")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)
    
    # Convert to grayscale
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    st.image(gray, caption="Grayscale Image", use_container_width=True, channels="GRAY")
    
    # Blur image
    blur = cv2.GaussianBlur(np.array(image), (15, 15), 0)
    st.image(blur, caption="Blurred Image", use_container_width=True)
    
