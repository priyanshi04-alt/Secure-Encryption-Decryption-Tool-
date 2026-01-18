import tkinter as tk
from tkinter import messagebox
import subprocess, sys, hashlib, base64

# ===== COLORS =====
BG = "#0d0d0d"
PANEL = "#161616"
TEXT = "#eaeaea"
ACCENT = "#00f7ff"
GREEN = "#00e676"

# ===== LOAD SALT =====
with open("salt.key", "rb") as f:
    SALT = f.read()

# ===== DEMO PASSWORD =====
CORRECT_PASSWORD = "secure123"

def derive_key(password):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        SALT,
        100000
    )
    return base64.urlsafe_b64encode(key)

def login():
    entered = password_entry.get()

    if entered == CORRECT_PASSWORD:
        derived_key = derive_key(entered)
        root.destroy()
        subprocess.Popen(
            [sys.executable, "gui_encrypt.py", derived_key.decode()]
        )
    else:
        messagebox.showerror("Access Denied", "Incorrect Password")

# ===== WINDOW =====
root = tk.Tk()
root.title("Secure Login")
root.geometry("420x320")
root.configure(bg=BG)

panel = tk.Frame(root, bg=PANEL)
panel.pack(expand=True, fill="both", padx=20, pady=20)

tk.Label(panel, text="SECURE LOGIN",
         font=("Segoe UI", 14, "bold"),
         fg=ACCENT, bg=PANEL).pack(pady=20)

tk.Label(panel, text="Enter Password",
         fg=TEXT, bg=PANEL).pack()

password_entry = tk.Entry(
    panel,
    show="*",
    bg="#000000",
    fg=TEXT,
    insertbackground=TEXT,
    font=("Consolas", 12),
    width=25,
    relief="flat"
)
password_entry.pack(pady=12)

tk.Button(panel, text="LOGIN",
          command=login,
          bg="#1b1b1b",
          fg=GREEN,
          font=("Segoe UI", 10, "bold"),
          width=18).pack(pady=20)

root.mainloop()
