import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Contact Form")
root.geometry("420x430")
root.configure(bg="#d3d3d3")

frame = tk.Frame(root, bg="#d3d3d3", bd=2, relief="groove", padx=20, pady=20)
frame.pack(pady=20)

# Заголовок
title = tk.Label(frame, text="Contact Form", font=("Helvetica", 18, "bold"), bg="#d3d3d3")
title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))

subtitle = tk.Label(frame, text="Please fill all entries.", font=("Helvetica", 10), bg="#d3d3d3")
subtitle.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 15))

# Функция для поля ввода
def create_labeled_entry(row, label_text):
    label = tk.Label(frame, text=label_text, font=("Helvetica", 10), bg="#d3d3d3")
    label.grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame, width=40)
    entry.grid(row=row, column=1, pady=5, sticky="w")
    return entry

# Поля ввода
name_entry = create_labeled_entry(2, "Name :")
email_entry = create_labeled_entry(3, "Email :")

# Поле сообщения
message_label = tk.Label(frame, text="Message :", font=("Helvetica", 10), bg="#d3d3d3")
message_label.grid(row=4, column=0, sticky="nw", pady=5)
message_entry = tk.Text(frame, width=38, height=5)
message_entry.grid(row=4, column=1, pady=5, sticky="w")

# Subject — надпись и выпадающий список
subject_label = tk.Label(frame, text="Subject :", font=("Helvetica", 10), bg="#d3d3d3")
subject_label.grid(row=5, column=0, sticky="w", pady=5)

subject_var = tk.StringVar()
subject_menu = ttk.Combobox(frame, textvariable=subject_var, state="readonly", width=37)
subject_menu['values'] = ["Product Inquiry", "Support", "Feedback", "Other"]
subject_menu.current(0)
subject_menu.grid(row=5, column=1, sticky="w", pady=5)

# Кнопка отправки
send_button = tk.Button(frame, text="Send", bg="#bcbcbc", fg="black", width=10)
send_button.grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()
