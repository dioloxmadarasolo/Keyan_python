import sqlite3
from datetime import datetime

# Создаем базу данных и таблицу
conn = sqlite3.connect('telemasterskaya.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tv_repairs
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                manufacturer TEXT,
                price REAL,
                repair_date TEXT,
                document TEXT,
                master TEXT,
                payment REAL)''')
conn.commit()


def add_repair():
    print("\nДобавление записи о ремонте:")
    brand = input("Марка телевизора: ")
    manufacturer = input("Завод-изготовитель: ")
    price = float(input("Цена: "))
    doc = input("Номер документа: ")
    master = input("ФИО мастера: ")
    payment = float(input("Сумма оплаты: "))

    # Получаем текущую дату в формате ДД.ММ.ГГГГ
    current_date = datetime.now().strftime("%d.%m.%Y")

    cursor.execute("INSERT INTO tv_repairs VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                   (brand, manufacturer, price, current_date, doc, master, payment))
    conn.commit()
    print("Запись добавлена!\n")


def show_all():
    print("\nВсе записи о ремонте:")
    cursor.execute("SELECT * FROM tv_repairs")
    repairs = cursor.fetchall()

    for repair in repairs:
        print(f"{repair[0]}. {repair[1]} ({repair[2]}), {repair[3]} руб.")
        print(f"Дата ремонта: {repair[4]}, Док: {repair[5]}, Мастер: {repair[6]}, Оплата: {repair[7]} руб.")
        print("-" * 40)


def edit_repair():
    show_all()
    repair_id = input("\nВведите ID записи для редактирования: ")

    cursor.execute("SELECT * FROM tv_repairs WHERE id=?", (repair_id,))
    repair = cursor.fetchone()

    if not repair:
        print("Запись с таким ID не найдена!")
        return

    print("\nТекущие данные записи:")
    print(f"1. Марка телевизора: {repair[1]}")
    print(f"2. Завод-изготовитель: {repair[2]}")
    print(f"3. Цена: {repair[3]}")
    print(f"4. Дата ремонта: {repair[4]}")
    print(f"5. Документ: {repair[5]}")
    print(f"6. Мастер: {repair[6]}")
    print(f"7. Сумма оплаты: {repair[7]}")

    field = input("\nВведите номер поля для редактирования (1-7): ")

    if field not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Неверный номер поля!")
        return

    new_value = input("Введите новое значение: ")

    # Для числовых полей преобразуем ввод
    if field in ['3', '7']:
        try:
            new_value = float(new_value)
        except ValueError:
            print("Ошибка: должно быть числовое значение!")
            return

    fields = ['brand', 'manufacturer', 'price', 'repair_date', 'document', 'master', 'payment']
    field_name = fields[int(field) - 1]

    cursor.execute(f"UPDATE tv_repairs SET {field_name}=? WHERE id=?", (new_value, repair_id))
    conn.commit()
    print("Запись успешно обновлена!")


def delete_repair():
    show_all()
    repair_id = input("\nВведите ID записи для удаления: ")

    cursor.execute("SELECT * FROM tv_repairs WHERE id=?", (repair_id,))
    repair = cursor.fetchone()

    if not repair:
        print("Запись с таким ID не найдена!")
        return

    confirm = input(f"Вы уверены, что хотите удалить запись {repair[1]} (ID: {repair[0]})? (y/n): ")
    if confirm.lower() == 'y':
        cursor.execute("DELETE FROM tv_repairs WHERE id=?", (repair_id,))
        conn.commit()
        print("Запись удалена!")
    else:
        print("Удаление отменено.")


def main():
    while True:
        print("\nТЕЛЕМАСТЕРСКАЯ - Учет ремонта телевизоров")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_repair()
        elif choice == '2':
            show_all()
        elif choice == '3':
            edit_repair()
        elif choice == '4':
            delete_repair()
        elif choice == '5':
            conn.close()
            print("Работа завершена")
            break
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()