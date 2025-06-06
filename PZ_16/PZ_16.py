class Animal:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def animal(self):
<<<<<<< HEAD
        print(f"Имя животного: {self.name}, вид: {self.type}")


dog = Animal("Олег", "Чихахуа")

cat = Animal("Кнопа", "Шотландская вислоухая кошка")

dog.animal()

cat.animal()
=======
        print(f"Имя животного: {self.name}, вид:{self.type}")

dog = Animal("Олег", "Чихахуа")
cat = Animal("Кнопа", "Шотландская вислоухая кошка")
dog.animal()
cat.animal()
>>>>>>> origin/main
