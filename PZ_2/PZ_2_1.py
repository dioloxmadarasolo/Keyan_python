# Дано двузначное число. Найти сумму и произведение его цифр.

# Ввод и проверка ввёл ли пользователь число или нет
try:
    a = int(input("Введите двузначное число: "))
except:
    print("Введите число!")
# Проверка двузначное число или нет
if 100 > a > 9:
    b = a % 10
    c = a // 10
    # Вывод
    print("Сумма цифр вашего числа:", b + c)
    print("Произведение цифр вашего числа:", b * c)
else:
    print("Введите двузначное число!")
