import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def display_area(self):
        print(f"The area of the circle with center {self.center} and radius {self.radius} is: {self.area()}")
center_point = Point(3, 4)
circle = Circle(center_point, 5)
circle.display_area()
