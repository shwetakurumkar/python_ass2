import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Label Font Style Changer")

is_bold = tk.BooleanVar()
is_bold.set(False)

font_size = tk.IntVar()
font_size.set(12)

font_family = tk.StringVar()
font_family.set("Arial")

def update_font():
    weight = "bold" if is_bold.get() else "normal"
    size = font_size.get()
    family = font_family.get()
    
    label.config(font=(family, size, weight))

label = tk.Label(root, text="Change my Font!", font=(font_family.get(), font_size.get(), "normal"))
label.pack(pady=20)

bold_check = tk.Checkbutton(root, text="Bold", variable=is_bold, command=update_font)
bold_check.pack()

size_frame = tk.LabelFrame(root, text="Font Size", padx=10, pady=10)
size_frame.pack(pady=10)

tk.Radiobutton(size_frame, text="12", variable=font_size, value=12, command=update_font).pack(anchor=tk.W)
tk.Radiobutton(size_frame, text="16", variable=font_size, value=16, command=update_font).pack(anchor=tk.W)
tk.Radiobutton(size_frame, text="20", variable=font_size, value=20, command=update_font).pack(anchor=tk.W)

family_frame = tk.LabelFrame(root, text="Font Family", padx=10, pady=10)
family_frame.pack(pady=10)

tk.Radiobutton(family_frame, text="Arial", variable=font_family, value="Arial", command=update_font).pack(anchor=tk.W)
tk.Radiobutton(family_frame, text="Times New Roman", variable=font_family, value="Times New Roman", command=update_font).pack(anchor=tk.W)
tk.Radiobutton(family_frame, text="Courier New", variable=font_family, value="Courier New", command=update_font).pack(anchor=tk.W)

root.mainloop()