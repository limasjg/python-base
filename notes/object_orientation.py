# Object Orientation is a programming paradigm that uses "objects" to design applications and computer programs. It utilizes several key concepts such as:
# - Encapsulation: Bundling data and methods that operate on that data within a single unit (object).
# - Inheritance: Creating new classes based on existing classes, inheriting their attributes and methods.
# - Polymorphism: The ability of an object to take many forms, allowing methods to be used across different types of objects.

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def accelerate(self):
#         print(f"The model {self.model} is speed up.")

from car import Car

car1 = Car("Cobalt", 2018, "gray", False)

print(car1.model)
car1.accelerate()
car1.stop()