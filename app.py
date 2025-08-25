import streamlit as st
import pandas as pd
import numpy as np
import cv2
from PIL import Image

# App title
st.title("Streamlit & OpenCV App")
st.write("Upload an image")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image using PIL
    image = Image.open(uploaded_file)
    img = np.array(image)

    # Convert to BGR if needed
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # OpenCV basics
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(img, (15, 15), 0)
    invert = cv2.bitwise_not(gray)
    sketch = cv2.divide(gray, 255 - cv2.GaussianBlur(invert, (21, 21), 0), scale=256)

    # Display images
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_column_width=True)

    st.subheader("Grayscale Image")
    st.image(gray, channels="GRAY", use_column_width=True)

    st.subheader("Blurred Image")
    st.image(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB), use_column_width=True)

    st.subheader("Sketch Effect")
    st.image(sketch, channels="GRAY", use_column_width=True)
