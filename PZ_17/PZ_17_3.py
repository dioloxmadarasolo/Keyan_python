import os

# 1. Перейти в PZ11 и вывести список файлов
os.chdir("PZ11")
files = [f for f in os.listdir() if os.path.isfile(f)]
print("Файлы в PZ11:", files)

# 2. Создать папки и переместить файлы
os.chdir("..")  # Возврат в корень проекта
os.mkdir("test")
os.mkdir("test/test1")
# Предположим, что файлы из P36 и P37 известны
os.rename("PZ6/PZ_6_1.py", "test/PZ_6_1.py")
os.rename("PZ6/PZ_6_2.py", "test/PZ_6_2.py")
os.rename("PZ7/PZ_7_1.py", "test/test1/PZ_7_1.py")
# Вывод размеров файлов в test
for f in os.listdir("test"):
    if os.path.isfile(f"test/{f}"):
        print(f"Размер {f}:", os.path.getsize(f"test/{f}"))

# 3. Найти файл с самым коротким именем в PZ11
os.chdir("PZ11")
shortest = min(os.listdir(), key=lambda x: len(os.path.basename(x)))
print("Самый короткий файл:", os.path.basename(shortest))

# 4. Открыть PDF-файл
os.chdir("../PZXX")  # Переход в папку с PDF
os.startfile("report.pdf")

# 5. Удалить test.txt
os.chdir("..")
os.remove("test/test1/PZ_7_1.py")