# Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.

english_russian = {"apple": "яблоко", "cake": "торт", "false": "ложь", "true": "истина",
                   "door": "дверь", "window": "окно", "keyboard": "клавиатура", "mouse": "мышь",
                   "monitor": "монитор", "table": "стол"}

a = list(english_russian.keys())

print(a)
b = str(input("Введите слово которое хотите перевести: "))
if b in a:
    print(f"Перевод слова - {english_russian[b]}")
else:
    print("Введенное слово отсутствует в списке!")
