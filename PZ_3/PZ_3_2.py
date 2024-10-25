import random as r

a = r.randint(-50, 50)
even = "Нечётное"
positive = "Отрицательное"
null = 0
if a % 2 == 0:
    even = "Чётное"
if a > 0:
    positive = "Положительное"
if a == 0:
    null = 1
if null == 1:
    print("Ваше число ноль!")
else:
    print(f"{a} Ваше число: {even}, {positive}")

