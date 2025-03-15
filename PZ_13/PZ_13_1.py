# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры)

matrix = [
    [42, 55, 10,5],
    [12, 1, 0, 4],
    [6, 90, 34, 8]
]
N = int(input("Введите номер столбца"))

def matSum(N):
    for i in range(len(matrix)):
        b = int(matrix[0][N]+matrix[i][N])
        print(b)

matSum(N)

print(len(matrix))
