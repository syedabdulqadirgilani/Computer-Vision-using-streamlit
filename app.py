# =========================
# Streamlit Computer Vision Project
# Blur & Sketch Effect (No Face Detection)
# =========================

import cv2
import streamlit as st
import numpy as np

# Streamlit App Title
st.title("Blur & Sketch App (No Face Detection)")
st.write("Upload an image and see the sketch effect!")

# Upload image
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image with OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)  # 1 means color image

    # Apply sketch effect to the whole image
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray_frame)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_frame, inverted_blur, scale=256.0)

    # Optionally, you can also blur the full image
    blur_full = cv2.GaussianBlur(img, (21, 21), 0)

    # Show results
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")

    st.subheader("Sketch Effect")
    st.image(sketch, channels="GRAY")

    st.subheader("Blurred Image")
    st.image(cv2.cvtColor(blur_full, cv2.COLOR_BGR2RGB), channels="RGB")

