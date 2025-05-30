#В двумерном списке найти отрицательные элементы, сформировать из них новый
#массив. Вывести размер полученного массива.

import random as r

X = int(input("Введите количество строк и столбцов матрицы: "))
matrix = [[r.randint(-100, 100) for i in range(X)] for i in range(X)]
print(matrix)
xirtam = [element for i in matrix for element in i if element < 0]

print(xirtam)
