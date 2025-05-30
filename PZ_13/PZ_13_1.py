# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры)

import random as r

X = int(input("Введите количество строк и столбцов матрицы: "))
matrix = [[r.randint(1, 100) for i in range(X)] for i in range(X)]

n = int(input("Введите номер столбца (отсчет с 0): "))

sum_elements = 0
product_elements = 1

for i in matrix:
    sum_elements += i[n]
    product_elements *= i[n]

print(f"Сумма элементов {n}-го столбца: {sum_elements}")
print(f"Произведение элементов {n}-го столбца: {product_elements}")
print(matrix)
