from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import tkinter as tk
from tkinter import filedialog, messagebox
import os

BLOCK_SIZE = 16  # AES block size
salt = b'secure_salt_1234'  # You can randomize it per user/session

def pad(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def get_key(password):
    return PBKDF2(password, salt, dkLen=32)

def encrypt_file(file_path, password):
    key = get_key(password)
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    try:
        with open(file_path, 'rb') as f:
            plaintext = f.read()
        ciphertext = cipher.encrypt(pad(plaintext))

        with open(file_path + '.enc', 'wb') as f:
            f.write(iv + ciphertext)
        return "✔️ Encryption successful!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def decrypt_file(file_path, password):
    key = get_key(password)
    try:
        with open(file_path, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext))

        output_file = file_path.replace('.enc', '.dec')
        with open(output_file, 'wb') as f:
            f.write(plaintext)
        return "✔️ Decryption successful!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ---------- GUI ----------
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def encrypt_action():
    file_path = file_entry.get()
    password = password_entry.get()
    if not file_path or not password:
        messagebox.showwarning("Input Error", "Please select file and enter password.")
        return
    result = encrypt_file(file_path, password)
    messagebox.showinfo("Encryption", result)

def decrypt_action():
    file_path = file_entry.get()
    password = password_entry.get()
    if not file_path or not password:
        messagebox.showwarning("Input Error", "Please select file and enter password.")
        return
    result = decrypt_file(file_path, password)
    messagebox.showinfo("Decryption", result)

# ---------- Main Window ----------
root = tk.Tk()
root.title("Advanced Encryption Tool - CODTECH")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="🔐 ADVANCED ENCRYPTION TOOL", font=("Helvetica", 16, "bold")).pack(pady=10)

file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse", command=browse_file)
browse_btn.pack(pady=5)

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

encrypt_btn = tk.Button(root, text="Encrypt File", width=20, command=encrypt_action)
encrypt_btn.pack(pady=5)

decrypt_btn = tk.Button(root, text="Decrypt File", width=20, command=decrypt_action)
decrypt_btn.pack(pady=5)

root.mainloop()
