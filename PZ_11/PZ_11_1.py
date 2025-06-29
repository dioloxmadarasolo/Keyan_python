# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Среднее арифметическое элементов первой трети:

import random


# 1. Формируем исходный файл с числами
def create_initial_file(filename, num_count=20):
    with open(filename, 'w') as f:
        # Генерируем случайные положительные и отрицательные числа
        numbers = [random.randint(-100, 100) for _ in range(num_count)]
        # Записываем числа в файл через пробел
        f.write(' '.join(map(str, numbers)))
    print(f"Создан файл {filename} с {num_count} числами")


# 2. Обрабатываем данные и создаем отчет
def process_data(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        data = f.read()

    # Преобразуем строку в список чисел
    numbers = list(map(int, data.split()))

    # Вычисляем требуемые значения
    count = len(numbers)
    max_num = max(numbers)

    # Вычисляем среднее первой трети
    third = len(numbers) // 3
    first_third = numbers[:third] if third > 0 else numbers
    avg_first_third = sum(first_third) / len(first_third) if first_third else 0

    # Формируем отчет
    report = f"""Исходные данные:
{' '.join(map(str, numbers))}

Количество элементов: {count}
Максимальный элемент: {max_num}
Среднее арифметическое элементов первой трети: {avg_first_third:.2f}"""

    # Записываем отчет в новый файл
    with open(output_filename, 'w') as f:
        f.write(report)

    print(f"Отчет сохранен в файл {output_filename}")


# Основная программа
if __name__ == "__main__":
    input_file = "numbers.txt"
    output_file = "report.txt"

    # Создаем исходный файл с числами
    create_initial_file(input_file)

    # Обрабатываем данные и создаем отчет
    process_data(input_file, output_file)

    # Выводим содержимое отчетного файла на экран
    print("\nСодержимое отчетного файла:")
    with open(output_file, 'r') as f:
        print(f.read())