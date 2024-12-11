# Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными
# номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не
# использовать.

import random as r
N = int(input("Введите длину списка. Обязательно нечётное! "))
A = []
B = []
for i in range(N):
    A.append(r.randint(-10, 10))

print(A)

for i in range(len(A)):
    B.append(A[i+2])


print(B)

print(len(A))