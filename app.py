# =========================
# Streamlit Computer Vision Project
# Blur & Sketch Effect (No Face Detection)
# =========================

import cv2
import streamlit as st
import numpy as np

# App title
st.title("Blur & Sketch App")
st.write("Upload an image to see the sketch and blur effects!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # --------- Sketch Effect ----------
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    # --------- Blur Effect ----------
    blur_img = cv2.GaussianBlur(img, (21, 21), 0)

    # Display images
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    st.subheader("Sketch Effect")
    st.image(sketch, channels="GRAY")

    st.subheader("Blurred Image")
    st.image(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
