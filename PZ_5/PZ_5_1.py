# Составить функцию, которая выполнит суммирования числового ряда

a = input()
b = list(a)
f = 0
print(b)


def summ(b):
    global f
    for i in range(len(b)):
        f = f + int(b[i])
    print(f)


summ(b)
