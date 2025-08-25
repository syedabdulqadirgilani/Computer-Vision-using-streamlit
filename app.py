# =========================
# Easy Streamlit + OpenCV App
# Blur & Sketch Effects
# Updated with latest versions
# =========================

import streamlit as st
import cv2
import numpy as np
from PIL import Image

# App title
st.set_page_config(page_title="Easy Blur & Sketch App", layout="centered")
st.title("Easy Blur & Sketch App")
st.write("Upload an image to see the sketch and blur effects!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image using PIL
    image = Image.open(uploaded_file)
    img = np.array(image)  # Convert to OpenCV format

    # Convert to BGR if needed
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # --------- OpenCV Basics ----------
    # 1️⃣ Convert to Gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2️⃣ Blur
    blur_img = cv2.GaussianBlur(img, (21, 21), 0)

    # 3️⃣ Sketch effect
    invert = cv2.bitwise_not(gray)
    blur_invert = cv2.GaussianBlur(invert, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur_invert, scale=256)

    # Display images
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_column_width=True)

    st.subheader("Grayscale Image")
    st.image(gray, channels="GRAY", use_column_width=True)

    st.subheader("Blurred Image")
    st.image(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB), use_column_width=True)

    st.subheader("Sketch Effect")
    st.image(sketch, channels="GRAY", use_column_width=True)
