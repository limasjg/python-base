# Inheritance Allows a class to inherit attributes and methods from another class.
# The class that is inherited from is called the "parent" or "base" class, while the class that inherits is called the "child" or "derived" class.

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("AU!AU!")

class Cat(Animal):
    def speak(self):
        print("MIAU!")

class Mouse(Animal):
    def speak(self):
        print("KIKI!")

dog = Dog("Cerberus")
cat = Cat("Luke")
mouse = Mouse("Mickey")

print(dog.name)
print(cat.name)
print(mouse.name)

dog.speak()
cat.speak()
mouse.speak()
