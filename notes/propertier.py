# @property decorator is used to define a method as a property, which allows you to access it like an attribute.
# Benefit is add additional logic when read, write, or delete attributes without changing the interface of the class.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be positive")
        
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            raise ValueError("Height must be positive")
        
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(5, 10)

rectangle.width = 7
rectangle.height = 12

del rectangle.width
del rectangle.height

# print(rectangle._width)  # Output: 5
# print(rectangle._height)  # Output: 10
