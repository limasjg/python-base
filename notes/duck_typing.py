#Duck Typing" is another way to achieve polymorphism in python.
# Object must have the minimum necessary atributes and methods to be used in a particular context.
# The name "Duck Typing" comes from the phrase "If it looks like a duck.

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")
    
class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    alive = False
    def speak(self):
        print("Vroom!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(f"Is alive: {animal.alive}")
    

