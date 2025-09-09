import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Error", "Password length must be at least 4.")
            return
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        password = generate_password(length, use_digits, use_symbols)
        result_label.config(text=password)
        with open("passwords.txt", "a") as f:
            f.write(password + "\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def clear_result():
    result_label.config(text="")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.columnconfigure(0, weight=1)

title_label = tk.Label(root, text="🔐 Password Generator", font=("Arial", 36, "bold"), bg="#1e1e1e", fg="#ffffff")
title_label.grid(row=0, column=0, pady=20, sticky="n")

length_frame = tk.Frame(root, bg="#1e1e1e")
length_frame.grid(row=1, column=0, pady=10)
tk.Label(length_frame, text="Password length:", font=("Arial", 18), bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=5)
length_entry = tk.Entry(length_frame, width=6, font=("Arial", 18), bg="#2e2e2e", fg="white")
length_entry.pack(side="left")
length_entry.insert(0, "12")

digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include digits", variable=digits_var, font=("Arial", 16), bg="#1e1e1e", fg="white", selectcolor="#3e3e3e").grid(row=2, column=0, sticky="n")
tk.Checkbutton(root, text="Include symbols", variable=symbols_var, font=("Arial", 16), bg="#1e1e1e", fg="white", selectcolor="#3e3e3e").grid(row=3, column=0, sticky="n")

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.grid(row=4, column=0, pady=20)

generate_btn = tk.Button(btn_frame, text="Generate Password", command=on_generate, font=("Arial", 16), bg="#4CAF50", fg="white", width=20, height=2)
generate_btn.pack(pady=5)

copy_btn = tk.Button(btn_frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 16), bg="#2196F3", fg="white", width=20, height=2)
copy_btn.pack(pady=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_result, font=("Arial", 16), bg="#f44336", fg="white", width=20, height=2)
clear_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 28), fg="#00ffff", bg="#1e1e1e")
result_label.grid(row=5, column=0, pady=15, sticky="n")

root.mainloop()
