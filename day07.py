import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print("도형의 면적을 출력합니다.")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width

    def __repr__(self):
        return f"사각형의 좌표는 {(self.x, self.y)} 넓이는 {self.get_area()}"

    def __add__(self, other):
        # 두 사가형 넓이의 합
        # return self.get_area() + other.get_area()
        # 각 사각형 width를 더하고, height를 더해 새로운 사각형 생성
        return Rectangle(0, 0, self.width + other.width, self.length + other.length)


class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height

    def get_area(self):
        return super().get_area() * self.height


c1 = Circle(1.0, 2.0, 10.0)
c2 = Circle(1.0, 2.0, 2.0)
r1 = Rectangle(50, 100, 5.0, 2.0)
r2 = Rectangle(10, 200, 10.0, 15.0)
cy1 = Cylinder(100, 100, 10.0, 2)
print(cy1.get_area())
print(f"사각형의 좌표는 {(r1.x, r1.y)} 넓이는 {r1.get_area()}")
print(c1.get_area())
print(c2.get_area())
print(r1)
print(r2)
print(r1 + r2)
