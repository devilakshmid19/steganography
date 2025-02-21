# Image Steganography with Python

This project demonstrates a simple implementation of image steganography using Python and OpenCV. The application allows users to hide (encrypt) a secret message inside an image and later retrieve (decrypt) the message using a simple UI built with Tkinter.

## Features

- **Data Hiding (Encryption):**  
  Embed a secret text message into a cover image. The program writes each character's ASCII value into the image pixels (using a diagonal embedding method) and saves the modified image as a lossless PNG file to preserve data integrity.

- **Decryption:**  
  Retrieve the hidden message from the modified image by providing the correct passcode and the message length.

- **Graphical User Interface (GUI):**  
  A simple Tkinter-based UI to facilitate the process of:
  - Uploading a cover image.
  - Entering the secret message and passcode.
  - Encrypting (hiding) the message in the image.
  - Uploading an encrypted image.
  - Decrypting (extracting) the hidden message.

## Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)  
  Install via pip:  
  ```bash
  pip install opencv-python
- [NumPy](https://pypi.org/project/numpy/)
  Install via pip:
  ```bash
  pip install numpy

## 🚀 Live Demo
- Try the Steganography App here:  
- [🔗 Click to Open](https://steganography.streamlit.app)

## Usage
- Run the program:
  ```bash
  python steganography.py

- Use the GUI to:

  - Upload an image for encryption.
  - Enter the secret message and passcode.
  - Encrypt the message and save the stego-image.
  - Load an encrypted image and decrypt the message.
## License
- This project is licensed under the MIT License. See the LICENSE file for details.

