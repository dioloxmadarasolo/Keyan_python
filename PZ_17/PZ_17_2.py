# Вариант 3 Задание 3

# 1. Дано целое число A. Проверить истинность высказывания: «Число A является
# четным».

# 2. Размер скидки на продукты определен следующим образом: при покупке до 500 р.
# скидка составит 2%; при покупке от 500 р. до 1000 р. скидка составит 3%; при
# покупке от 1000 р. до 1500 р. скидка составит 4%; при покупке от 1500 р. до 2000 р.
# скидка составит 5%. Составить программу определяющую размер скидки в
# зависимости от потраченной суммы.




import tkinter as tk
from tkinter import messagebox

def check_even():
    try:
        a = int(entry_a.get())
        if a % 2 == 0:
            result_even.set(f"Число {a} является чётным.")
        else:
            result_even.set(f"Число {a} не является чётным.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число.")

def calculate_discount():
    try:
        amount = float(entry_amount.get())
        if amount < 0:
            raise ValueError
        if amount < 500:
            discount = 2
        elif amount < 1000:
            discount = 3
        elif amount < 1500:
            discount = 4
        elif amount <= 2000:
            discount = 5
        else:
            discount = 0
        result_discount.set(f"Скидка: {discount}%")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную сумму (неотрицательное число).")

# Окно
root = tk.Tk()
root.title("Проверка чётности и расчёт скидки")
root.geometry("400x300")
root.resizable(False, False)

# Задание 1
tk.Label(root, text="Задание 1: Проверка чётности").pack(pady=(10, 0))
entry_a = tk.Entry(root)
entry_a.pack()
btn_check = tk.Button(root, text="Проверить", command=check_even)
btn_check.pack(pady=5)
result_even = tk.StringVar()
tk.Label(root, textvariable=result_even, fg="blue").pack()

# Разделитель
tk.Label(root, text="").pack()

# Задание 2
tk.Label(root, text="Задание 2: Расчёт скидки").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()
btn_discount = tk.Button(root, text="Рассчитать скидку", command=calculate_discount)
btn_discount.pack(pady=5)
result_discount = tk.StringVar()
tk.Label(root, textvariable=result_discount, fg="green").pack()

root.mainloop()
