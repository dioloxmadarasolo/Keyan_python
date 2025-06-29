# Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно вставив после каждой строки строку из символов
# «*».

import os

# Проверяем существование файла
file_name = 'text18-12.txt'
if not os.path.exists(file_name):
    print(f"Файл {file_name} не найден!")
    print(f"Текущая папка: {os.getcwd()}")
    exit()

# Пробуем разные кодировки для чтения файла
encodings = ['utf-8', 'cp1251', 'utf-16']  # Основные кодировки для русского текста

content = None
for encoding in encodings:
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            content = file.read()
        print(f"Файл прочитан в кодировке {encoding}")
        break
    except UnicodeDecodeError:
        continue

if content is None:
    print("Не удалось прочитать файл. Попробуйте сохранить его в UTF-8 или ANSI (Windows-1251)")
    exit()

# 1. Выводим содержимое файла
print("\nСодержимое файла:")
print(content)

# 2. Подсчитываем пробельные символы
space_count = content.count(' ')
newline_count = content.count('\n')
tab_count = content.count('\t')
total_whitespace = space_count + newline_count + tab_count

print("\nКоличество пробельных символов:")
print(f"Пробелы: {space_count}")
print(f"Переносы строк: {newline_count}")
print(f"Табуляции: {tab_count}")
print(f"Всего: {total_whitespace}")

# 3. Создаём новый файл с добавлением строк из '*'
lines = content.split('\n')
modified_lines = []
for line in lines:
    if line.strip():  # Пропускаем пустые строки
        modified_lines.append(line)
        modified_lines.append('*' * len(line))

modified_content = '\n'.join(modified_lines)

# Сохраняем в новый файл (в UTF-8)
output_file = 'modified_' + file_name
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(modified_content)

print(f"\nФайл {output_file} успешно создан!")