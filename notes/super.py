# super() = Function used in a child class to call a method from the parent class (superclass).
# Allows you to extend the functionality of the inherited method.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"This shape is {self.color} and {'filled' if self.filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # Call the __init__ method of the parent class (Shape)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2:.2f}cm.")
        super().describe() # Call the describe method of the parent class (Shape)

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled) # Call the __init__ method of the parent class (Shape)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled) # Call the __init__ method of the parent class (Shape)
        self.width = width
        self.height = height

circle = Circle("Red", True, 5)
square = Square("Blue", False, 10)
triangle = Triangle("Green", True, 5, 10)

print(circle.color)
print(square.color)
print(triangle.color)

circle.describe()
square.describe()
triangle.describe()