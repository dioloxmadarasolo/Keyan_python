# Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.

english_russian = {"apple": "яблоко", "cake": "торт", "false": "ложь", "true": "истина", "door": "дверь", "window": "окно", "keyboard": "клавиатура", "mouse": "мышь", "monitor": "монитор", "table": "стол"}
a = english_russian.keys()
print(a)
b = input("Введите слово которое хотите перевести: ")

print(english_russian[b])
