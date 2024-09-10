import random

class Mother:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"Я мама, зовут {self._name}"

class Daughter(Mother):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def __str__(self):
        return f"Я дочь, зовут {self._name}, мне {self._age} лет"

mother = Mother('')
daughter = Daughter('', 10)

names = ["Катя", "Оля", "Ира", "Лена", "Таня"]

mother._name = random.choice(names)
daughter._name = random.choice(names)

print(mother)
print(daughter)
