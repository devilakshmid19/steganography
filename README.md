Image Steganography with Python

This project demonstrates a simple implementation of image steganography using Python and OpenCV. The application allows users to hide (encrypt) a secret message inside an image and later retrieve (decrypt) the message using a simple UI built with Tkinter.

Features

Data Hiding (Encryption):Embed a secret text message into a cover image. The program writes each character's ASCII value into the image pixels (using a diagonal embedding method) and saves the modified image as a lossless PNG file to preserve data integrity.

Decryption:Retrieve the hidden message from the modified image by providing the correct passcode and the message length.

Graphical User Interface (GUI):A simple Tkinter-based UI to facilitate the process of:

Uploading a cover image.

Entering the secret message and passcode.

Encrypting (hiding) the message in the image.

Uploading an encrypted image.

Decrypting (extracting) the hidden message.

Requirements

Ensure you have Python 3.x installed. Install the required dependencies using:

pip install opencv-python numpy pillow tkinter

How It Works

Encryption Process:

The user uploads a cover image (PNG format recommended).

The secret message and a passcode (for added security) are entered.

The algorithm encodes each character’s ASCII value into pixel intensity values along the image diagonally.

The modified image is saved as a new PNG file to ensure lossless data storage.

Decryption Process:

The user uploads the modified (stego) image.

The passcode and message length are provided to extract the hidden message.

The program reads the encoded pixel values, reconstructs the ASCII characters, and reveals the original message.

Usage

Run the program:

python steganography.py

Use the GUI to:

Upload an image for encryption.

Enter the secret message and passcode.

Encrypt the message and save the stego-image.

Load an encrypted image and decrypt the message.

Security Considerations

The passcode ensures that only authorized users can decrypt the message.

Using lossless PNG images prevents data corruption from compression artifacts.

Encryption strength depends on message length and pixel distribution.

Future Improvements

Implement a more robust encoding method using LSB (Least Significant Bit) technique.

Add support for different image formats like JPEG (with some quality loss considerations).

Improve UI/UX with additional options for customization.

Enhance security by integrating AES encryption before embedding the text.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.
