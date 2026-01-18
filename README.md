# 🔐 Secure Encryption & Decryption Tool  
### Password-Based Key Derivation | Cyber Dark UI | Python

A **cybersecurity-focused Python application** that securely encrypts and decrypts data using a **password-derived cryptographic key**.  
The project demonstrates **real-world security practices** such as authentication, key derivation, encryption, and session handling.

---

## 🚀 Features

- 🔑 **Login Authentication**
- 🔐 **Password → Key Derivation (PBKDF2 + Salt)**
- 🧠 **AES-based Symmetric Encryption (Fernet)**
- 🖥️ **Modern Dark / Neon Cyber UI**
- 🧹 Clear Input / Output
- 📋 Copy Encrypted / Decrypted Text
- 🔁 **Logout (Secure Session Termination)**

---

## 🧠 Security Workflow

Password
↓
PBKDF2 + Salt
↓
Derived Encryption Key
↓
Encrypt / Decrypt Data

✔ Password is **never used directly** as an encryption key  
✔ Wrong password → decryption fails  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **GUI:** Tkinter  
- **Cryptography:** cryptography (Fernet / AES)  
- **Key Derivation:** PBKDF2 (SHA-256)  
- **UI Theme:** Dark Cyber / Neon  

---

## 📁 Project Structure

EncryptionProject/
│
├── generate_salt.py # Generates salt (run once)
├── salt.key # Stores cryptographic salt
├── login_gui.py # Login screen (start here)
├── gui_encrypt.py # Encryption & decryption GUI
└── README.md

---
```md
## ⚙️ Installation

### 1️⃣ Install Python (3.10+)
```bash
python --version

2️⃣ Install Dependencies
pip install cryptography

▶️ How to Run
Step 1: Generate Salt (Only Once)
python generate_salt.py
Step 2: Start the Application
python login_gui.py
🔑 Demo Login
Password: secure123
⚠️ Password is hardcoded for demo / academic purposes only.

🧩 Application Modules
Login Module – Authenticates user
Key Derivation Module – Generates secure key using PBKDF2
Encryption Module – Converts plaintext → ciphertext
Decryption Module – Restores original data
Session Management – Logout clears active key

🎓 Academic Use
Mini Project / IP
Cybersecurity demonstration
Final-year project base
Resume / GitHub portfolio

🚀 Future Enhancements
Store hashed passwords instead of hardcoding
Add file encryption (PDF, TXT, Images)
Multi-user authentication system
Client-server encrypted communication
Two-factor authentication (2FA)

👩‍💻 Author
Priyanshi
Computer Science & Engineering

📜 License
This project is for educational purposes only.


