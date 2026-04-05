# Polymorphism is greek word that means many forms.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2
    
class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)    

    
shapes = [Circle(5), Square(10), Triangle(5, 10), Pizza("Pepperoni", 12)]

for shape in shapes:
    print(f"{shape.area()}cm^2")