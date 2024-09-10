class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height
g=1
while g==1:
    a=int(input("Введите ширину треугольника"))
    b=int(input("Введите высоту треугольника"))
    c=int(input("Введите ширину прямоугольника"))
    d=int(input("Введите высоту прямоугольника"))
    if a>0 and b>0 and c>0 and d>0:
        g=2
    else:
        print("\n\n\n\n\nВводи только положительные числа")
        g=1
triangle = Triangle(a, b)
rectangle = Rectangle(c, d)

print(f"Площадь треугольника: {triangle.area()}")
print(f"Площадь прямоугольника: {rectangle.area()}")
