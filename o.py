class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_description(self):
        return f"Имя: {self._name}, Возраст: {self._age}"

class Slon(Animal):
    def get_description(self):
        return f"{super().get_description()}, Вид: Slon"

class Lion(Animal):
    def get_description(self):
        return f"{super().get_description()}, Вид: lion"


Slon = Slon("Шизняк", 5)
Lion = Lion("Бабиджон", 10)

print(Slon.get_description())
print(Lion.get_description())
