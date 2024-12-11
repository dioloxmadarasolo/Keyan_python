# Составить функцию, которая выполнит суммирования числового ряда

try:
    a = int(input("Введите числовой ряд слитно: "))

except ValueError:
    print("Что-то пошло не так. Введите число!")

else:
    c = str(a)
    numbers = list(c)
    print(numbers)


    def summ(numbers):
        f = 0
        for i in range(len(numbers)):
            f = f + int(numbers[i])
        print(f)


    summ(numbers)
