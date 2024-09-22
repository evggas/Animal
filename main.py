
import json

# Базовый класс Animal для всех животных
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен подклассом")

    def eat(self):
        print(f"{self.name} ест.")

# Подкласс Bird для птиц
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Размах крыльев

    def make_sound(self):
        print(f"{self.name} чирикает.")

    def fly(self):
        print(f"{self.name} летает с размахом крыльев {self.wing_span} м.")

# Подкласс Mammal для млекопитающих
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Цвет шерсти

    def make_sound(self):
        print(f"{self.name} рычит.")

# Подкласс Reptile для рептилий
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Тип чешуи

    def make_sound(self):
        print(f"{self.name} шипит.")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс Zoo для управления зоопарком
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    # Метод для добавления животного
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    # Метод для добавления сотрудника
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} нанят в зоопарк.")

    # Показать всех животных
    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name}, {animal.__class__.__name__}, возраст: {animal.age}")

    # Показать всех сотрудников
    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee.name}, должность: {employee.__class__.__name__}")

    # Сохранить данные зоопарка в файл (обновлённая версия)
    def save_to_file(self, filename):
        data = {
            "animals": [],
            "employees": [{"type": employee.__class__.__name__, "name": employee.name} for employee in self.employees]
        }

        for animal in self.animals:
            animal_data = {"type": animal.__class__.__name__, "name": animal.name, "age": animal.age}
            if isinstance(animal, Bird):
                animal_data["wing_span"] = animal.wing_span
            elif isinstance(animal, Mammal):
                animal_data["fur_color"] = animal.fur_color
            elif isinstance(animal, Reptile):
                animal_data["scale_type"] = animal.scale_type
            data["animals"].append(animal_data)

        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Данные зоопарка сохранены в файл {filename}.")

    # Загрузить данные зоопарка из файла (обновлённая версия)
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.animals = []
            for animal_data in data["animals"]:
                if animal_data["type"] == "Bird":
                    animal = Bird(animal_data["name"], animal_data["age"], animal_data["wing_span"])
                elif animal_data["type"] == "Mammal":
                    animal = Mammal(animal_data["name"], animal_data["age"], animal_data["fur_color"])
                elif animal_data["type"] == "Reptile":
                    animal = Reptile(animal_data["name"], animal_data["age"], animal_data["scale_type"])
                self.animals.append(animal)

            self.employees = [globals()[employee["type"]](employee["name"]) for employee in data["employees"]]
        print(f"Данные зоопарка загружены из файла {filename}.")

# Класс ZooKeeper для сотрудников-зоокиперов
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

# Класс Veterinarian для ветеринаров
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Пример использования программы
if __name__ == "__main__":
    # Создаем зоопарк
    my_zoo = Zoo()

    # Добавляем животных
    bird = Bird("Попугай", 2, 1.0)
    mammal = Mammal("Лев", 4, "золотистая")
    reptile = Reptile("Змея", 3, "гладкая чешуя")

    my_zoo.add_animal(bird)
    my_zoo.add_animal(mammal)
    my_zoo.add_animal(reptile)

    # Добавляем сотрудников
    zookeeper = ZooKeeper("Алекс")
    vet = Veterinarian("Доктор Айболит")

    my_zoo.add_employee(zookeeper)
    my_zoo.add_employee(vet)

    # Показать всех животных и сотрудников
    my_zoo.show_animals()
    my_zoo.show_employees()

    # Полиморфизм: звуки животных
    animal_sound([bird, mammal, reptile])

    # Сохранение и загрузка данных
    my_zoo.save_to_file("zoo_data.json")

    new_zoo = Zoo()
    new_zoo.load_from_file("zoo_data.json")
    new_zoo.show_animals()
    new_zoo.show_employees()
