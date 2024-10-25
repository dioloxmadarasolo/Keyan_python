import random as r

a = r.randint(-50, 50)

b = r.randint(-50, 50)

c = r.randint(-50, 50)

if a>0 and b>0 and c>0:
    print("Высказывание верно!")
    print(f"Ваши числа {a}, {b}, {c}")
else:
    print("Высказывание неверно!")
    print(f"Ваши числа {a}, {b}, {c}")
