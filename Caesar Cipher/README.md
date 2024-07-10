# Caesar Cipher App

This is a simple command-line application that implements the Caesar Cipher encryption and decryption algorithm.

## How the Caesar Cipher Works

The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. 

## Features

- **Encode**: Shift the letters of your message to create a ciphertext.
- **Decode**: Revert the shifted letters of a ciphertext to recover the original message.
- **Handles non-alphabet characters**: Non-alphabet characters (like spaces and punctuation) are not altered.
- **Repeatable**: Allows users to encode/decode multiple messages without restarting the application.

## Running the App

To run the app, ensure you have Python installed. Then, execute the following command in your terminal:

```bash
python caesar_cipher.py
```
## User Instructions

1. **Choose the mode:**
    - Type `encode` to encrypt a message.
    - Type `decode` to decrypt a message.
2. **Enter your message:** Type the message you want to encode or decode.
3. **Enter the shift number:** Type the number of positions you want to shift the alphabet by.
4. **See the result:** The app will display the encoded or decoded message.
5. **Repeat or Exit:** You can choose to encode/decode another message or exit the app.