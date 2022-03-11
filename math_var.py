import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_circle_area(self):
        return math.pi * (self.radius ** 2)
circle = Circle(10)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_circle_area())
print()

class Circle2:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_circle_area(self):
        return math.pi * (self.__radius ** 2)
circle = Circle2(10)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_circle_area())
#print("#__radius에 접근")
#print(circle.__radius)     접근 시 예외 발생
print()

class Circle3:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_circle_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle3(10)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_circle_area())
print()

print("#__radius에 접근")
print(circle.get_radius())
print()

circle.set_radius(2)
print("#반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_circle_area())