import streamlit as st
import cv2
import numpy as np

st.title("🔒 Image Steganography App")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    image = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    message = st.text_input("Enter the secret message")

    if st.button("Encrypt & Save"):
        if message:
            # Simple embedding by modifying pixel values
            for i, char in enumerate(message):
                image[i % image.shape[0], i % image.shape[1], 0] = ord(char)
            
            cv2.imwrite("stego_image.png", image)
            st.success("Message embedded! Download the image below.")
            st.download_button("Download Encrypted Image", data=open("stego_image.png", "rb"), file_name="stego_image.png")

    if st.button("Decrypt Message"):
        decrypted_message = ""
        for i in range(len(message)):
            decrypted_message += chr(image[i % image.shape[0], i % image.shape[1], 0])

        st.write("Decrypted Message:", decrypted_message)
