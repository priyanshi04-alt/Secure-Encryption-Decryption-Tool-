import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import subprocess, sys

# ===== GET DERIVED KEY =====
derived_key = sys.argv[1].encode()
cipher = Fernet(derived_key)

# ===== COLORS =====
BG = "#0d0d0d"
PANEL = "#161616"
TEXT = "#eaeaea"
ACCENT = "#00f7ff"
GREEN = "#00e676"
BTN_BG = "#1b1b1b"
BTN_UTIL = "#222222"
RED = "#ff5252"

# ===== FUNCTIONS =====
def encrypt_text():
    msg = text_input.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Warning", "Enter some text")
        return
    encrypted = cipher.encrypt(msg.encode())
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, encrypted.decode())

def decrypt_text():
    try:
        msg = text_input.get("1.0", tk.END).strip()
        decrypted = cipher.decrypt(msg.encode())
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, decrypted.decode())
    except:
        messagebox.showerror("Error", "Invalid encrypted text")

def clear_input():
    text_input.delete("1.0", tk.END)

def clear_output():
    text_output.delete("1.0", tk.END)

def copy_output():
    data = text_output.get("1.0", tk.END).strip()
    if not data:
        messagebox.showwarning("Warning", "Nothing to copy")
        return
    root.clipboard_clear()
    root.clipboard_append(data)
    messagebox.showinfo("Copied", "Output copied")

def logout():
    root.destroy()
    subprocess.Popen([sys.executable, "login_gui.py"])

# ===== WINDOW =====
root = tk.Tk()
root.title("Secure Encryption Tool")
root.geometry("580x640")
root.configure(bg=BG)

# ===== LOGOUT BUTTON =====
tk.Button(
    root,
    text="LOGOUT",
    command=logout,
    bg=BTN_BG,
    fg=RED,
    font=("Segoe UI", 9, "bold"),
    relief="flat",
    width=10
).pack(anchor="ne", padx=15, pady=8)

# ===== TITLE =====
tk.Label(
    root,
    text="SECURE ENCRYPTION & DECRYPTION",
    font=("Segoe UI", 14, "bold"),
    fg=ACCENT,
    bg=BG
).pack(pady=10)

# ===== INPUT PANEL =====
input_frame = tk.Frame(root, bg=PANEL)
input_frame.pack(padx=18, pady=10, fill="x")

tk.Label(input_frame, text="Input Text",
         fg=TEXT, bg=PANEL).pack(anchor="w", padx=12, pady=6)

text_input = tk.Text(
    input_frame,
    height=6,
    bg="#000000",
    fg=TEXT,
    insertbackground=TEXT,
    font=("Consolas", 11),
    relief="flat"
)
text_input.pack(padx=12, pady=6, fill="x")

# ===== ACTION BUTTONS =====
action_frame = tk.Frame(root, bg=BG)
action_frame.pack(pady=16)

tk.Button(action_frame, text="ENCRYPT",
          command=encrypt_text,
          bg=BTN_BG, fg=GREEN,
          font=("Segoe UI", 10, "bold"),
          width=16).grid(row=0, column=0, padx=12)

tk.Button(action_frame, text="DECRYPT",
          command=decrypt_text,
          bg=BTN_BG, fg=ACCENT,
          font=("Segoe UI", 10, "bold"),
          width=16).grid(row=0, column=1, padx=12)

# ===== UTILITY BUTTONS =====
util_frame = tk.Frame(root, bg=BG)
util_frame.pack(pady=6)

tk.Button(util_frame, text="🧹 Clear Input",
          command=clear_input,
          bg=BTN_UTIL, fg=ACCENT,
          width=16).grid(row=0, column=0, padx=8)

tk.Button(util_frame, text="🧹 Clear Output",
          command=clear_output,
          bg=BTN_UTIL, fg=ACCENT,
          width=16).grid(row=0, column=1, padx=8)

tk.Button(util_frame, text="📋 Copy Output",
          command=copy_output,
          bg=BTN_UTIL, fg=GREEN,
          width=16).grid(row=0, column=2, padx=8)

# ===== OUTPUT PANEL =====
output_frame = tk.Frame(root, bg=PANEL)
output_frame.pack(padx=18, pady=18, fill="x")

tk.Label(output_frame, text="Output",
         fg=TEXT, bg=PANEL).pack(anchor="w", padx=12, pady=6)

text_output = tk.Text(
    output_frame,
    height=6,
    bg="#000000",
    fg=ACCENT,
    insertbackground=ACCENT,
    font=("Consolas", 11),
    relief="flat"
)
text_output.pack(padx=12, pady=6, fill="x")

root.mainloop()
