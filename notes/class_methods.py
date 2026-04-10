# Class methods allow operations related to the class itself.
# Take (cls) as the first parameter instead of (self).

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    #CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return "No students to calculate average GPA."
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Alice", 3.8)
student2 = Student("Bob", 3.5)

print(Student.get_count())  # Output: Total students: 2
print(Student.average_gpa())  # Output: Average GPA: 3.65