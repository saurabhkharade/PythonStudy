class Shape:
    def area(self):
        print("Area formula not defined")


class Square(Shape):
    def area(self):
        print("Area of Square = side * side")


class Circle(Shape):
    def area(self):
        print("Area of Circle = π * r * r")


square = Square()
square.area()

circle = Circle()
circle.area()
