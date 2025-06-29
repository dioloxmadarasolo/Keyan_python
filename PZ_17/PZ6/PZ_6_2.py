# Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
# и вывести эти элементы в порядке возрастания их индексов

import random as r

N = int(input("Введите длину списка: "))

A = []
if N >=2:
    for i in range(N):
        A.append(r.randint(1,23))

    print(A)

    max_sum = A[0] + A[1]
    pair = (A[0], A[1])

    for i in range(1, len(A) - 1):
        current_sum = A[i] + A[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum
            pair = (A[i], A[i + 1])

    print(f"Максимальная пара: {min(pair)} и {max(pair)}.")

else:
    print("Список слишком короткий")
