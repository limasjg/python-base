# While loop = Execute some code WHILE a condition is true

# name = input("What is your name? ")

# while name == "":
#     print("You must enter a name.")
#     name = input("What is your name? ")
# print(f"Hello, {name}!")

# age = int(input("Enter your age: "))
# # Validate age input
# while age < 0 or age > 120:
#     print("Invalid age. Please enter a valid age between 0 and 120.")
#     age = int(input("Enter your age: "))
# print(f"Your age is {age}.")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}!")
#     food = input("Enter another food you like (q to quit): ")
# print("Bye!")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")