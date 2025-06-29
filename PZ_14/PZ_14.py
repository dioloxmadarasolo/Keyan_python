# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

# Чтение исходного файла
with open('dates.txt', 'r', encoding='utf-8') as file:
    dates = file.read().splitlines()

# Инициализация счетчиков
dot_format_count = 0
slash_format_count = 0
february_dates = []

# Шаблоны для поиска дат
dot_pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
slash_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
any_pattern = re.compile(r'^\d{2}[./,]\d{2}[./,]\d{4}$')

# Обработка каждой даты
for date in dates:
    # Нормализация разделителей (заменяем все разделители на /)
    normalized = re.sub(r'[.,]', '/', date)

    # Проверка форматов
    if dot_pattern.match(date):
        dot_format_count += 1
    elif slash_pattern.match(date):
        slash_format_count += 1

    # Проверка, что это февраль (месяц = 02)
    if any_pattern.match(date) and normalized.split('/')[1] == '02':
        february_dates.append(normalized)

# Запись результатов в новый файл
with open('february_dates.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(february_dates))

# Вывод статистики
print(f"Количество дат в формате ДД.ММ.ГГГГ: {dot_format_count}")
print(f"Количество дат в формате ДД/ММ/ГГГГ: {slash_format_count}")
print(f"Всего дат февраля: {len(february_dates)}")
print(f"Результат сохранен в файл february_dates.txt")
