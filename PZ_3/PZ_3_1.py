#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A, B, C положительное».

import random as r

a = r.randint(-50, 50)

b = r.randint(-50, 50)

c = r.randint(-50, 50)

if a>0 and b>0 and c>0:
    print(f"Ваши числа {a}, {b}, {c}")
    print("Высказывание верно!")
else:
    print(f"Ваши числа {a}, {b}, {c}")
    print("Высказывание неверно!")
