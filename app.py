# =========================
# Streamlit Computer Vision Project
# Blur & Sketch Effect (No Face Detection)
# Updated for latest versions
# =========================

import streamlit as st
import numpy as np
import cv2
from PIL import Image

# App configuration
st.set_page_config(page_title="Blur & Sketch App", layout="centered")
st.title("Blur & Sketch App")
st.write("Upload an image to see the sketch and blur effects!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image with PIL
    image = Image.open(uploaded_file)
    img = np.array(image)  # Convert PIL Image to NumPy array

    # Handle different image formats
    if len(img.shape) == 2:  # grayscale
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:  # RGBA
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else:  # RGB
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # --------- Sketch Effect ----------
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    # --------- Blur Effect ----------
    blur_img = cv2.GaussianBlur(img, (21, 21), 0)

    # Display images
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_column_width=True)

    st.subheader("Sketch Effect")
    st.image(sketch, channels="GRAY", use_column_width=True)

    st.subheader("Blurred Image")
    st.image(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB), use_column_width=True)
