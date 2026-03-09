# Class object shared among all instances of a class, defined outside the constructor
# Allow share data among all objects created from class

class Student:

    class_year = 2024
    number_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_of_students += 1

student1 = Student("John", 33)
student2 = Student("Peter", 29)

# print(student1.name, student1.age)

print(student1.class_year, Student.class_year)
print(Student.number_of_students)