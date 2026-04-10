# Static methods are methods that belong to a class rather than any object from that class.

# Instance methods = Best for operations on instances of class. (objects)

# Static methods = Best for utility functions that don't need access to instance or class data.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions
    
employee1 = Employee("Alice", "Developer")
print(Employee.is_valid_position("Developer"))  # Output: True
print(employee1.get_info())  # Output: Alice works as a Developer
