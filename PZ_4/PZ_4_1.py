# Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки чередуются). Условный оператор не использовать.
try:
    N = int(input("Введите число больше нуля: "))

except ValueError:
   print("Введите число!")

summ = 0
pm = True

if N > 0:
    for i in range(1, N + 1):
        if pm:
            summ += 1 / i
        else:
            summ -= 1 / i
        pm = not pm
        print(summ)
else:
    print("N должно быть больше 0!")
