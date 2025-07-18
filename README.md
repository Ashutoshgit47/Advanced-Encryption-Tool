# 🔐 Advanced Encryption Tool 

A secure, user-friendly Python GUI application for encrypting and decrypting files using **AES encryption (CBC mode)** with password-based key derivation. This tool ensures your files are safely encrypted with a modern cryptographic approach and offers an intuitive interface built with Tkinter.

---

## 🧩 Features

- ✅ AES-256 encryption in CBC mode  
- ✅ Password-based key derivation using PBKDF2  
- ✅ Simple, clean GUI using Tkinter  
- ✅ Secure IV handling (stored in encrypted file)  
- ✅ File padding/unpadding for block-aligned encryption  
- ✅ Works offline – no internet connection needed  
- ✅ No file size limit (text, images, PDFs, etc.)

---

## 📦 Requirements

Install the required Python package using:

```bash
pip install pycryptodome
```

---

## 🚀 How to Run

🔧 Step-by-step:
Clone this repository or download the script:

```bash
git clone https://github.com/Ashutoshgit47/Advanced-Encryption-Tool.git
cd Advanced-Encryption-Tool
```
Run the script:

python encryption_tool.py
✅ Ensure Python 3.7+ is installed.

---

## 🖥️ GUI Usage

Browse to select the file you want to encrypt/decrypt.

Enter a password (used to derive the encryption key).

Click "Encrypt File" or "Decrypt File".

Output files will be saved as:

🔒 Encrypted: filename.ext.enc

🔓 Decrypted: filename.ext.dec

---

## 🔐 How It Works

AES-256 (CBC Mode): Used for actual file encryption.

PBKDF2: Derives a secure key from your password and a fixed salt.

IV (Initialization Vector): Randomly generated for each file and prepended to the ciphertext.

Padding: PKCS-style padding ensures file size aligns to AES block size.

---

## 📁 Example

Original file: notes.txt

After encryption: notes.txt.enc

After decryption: notes.txt.dec

## ⚠️ Security Notice

🔐 This tool uses a fixed salt for simplicity.
For production use, generate a random salt per session.

❗ If you forget your password, encrypted files cannot be recovered.

🚫 Never transmit passwords or encrypted files over unsecured channels.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Credits

Developed by @Ashutoshgit47

Made with 💻 in Python + Tkinter + PyCryptodome
