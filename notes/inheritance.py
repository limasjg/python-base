# Inheritance Allows a class to inherit attributes and methods from another class.
# The class that is inherited from is called the "parent" or "base" class, while the class that inherits is called the "child" or "derived" class.

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("AU!AU!")

# class Cat(Animal):
#     def speak(self):
#         print("MIAU!")

# class Mouse(Animal):
#     def speak(self): 
#         print("KIKI!")

# dog = Dog("Cerberus")
# cat = Cat("Luke")
# mouse = Mouse("Mickey")

# print(dog.name)
# print(cat.name)
# print(mouse.name)

# dog.speak()
# cat.speak()
# mouse.speak()


# Multiple Inheritance allows a class to inherit from more than one parent class. C(A, B) means that class C inherits from both class A and class B.
# Multilevel Inheritance allows a class to inherit from a parent class, which in turn inherits from another parent class. A -> B -> C means that class B inherits from class A, and class C inherits from class B.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Pray(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predators(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Pray):
    pass

class Hawk(Predators):
    pass

class Fish(Pray, Predators):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt()
            