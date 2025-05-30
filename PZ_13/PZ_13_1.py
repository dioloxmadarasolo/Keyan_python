# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

n = int(input("Введите номер столбца (отсчет с 0): "))

sum_elements = 0
product_elements = 1

for i in matrix:
    sum_elements += i[n]
    product_elements *= i[n]

print(f"Сумма элементов {n}-го столбца: {sum_elements}")
print(f"Произведение элементов {n}-го столбца: {product_elements}")