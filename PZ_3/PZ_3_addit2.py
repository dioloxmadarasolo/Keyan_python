#Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.

a = int(input())
b = 0
if a % 2 == 0:
    b = int((a/4))
else:
    b = int((a*5))
print(b)