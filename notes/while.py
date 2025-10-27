# while execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You did NOT enter your name.")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# game = input("Enter a game that you like ('q' to quit): ").lower()

# while not game == "q":
#     print(f"You like {game}")
#     game = input("Enter an other game that you like ('q' to quit): ").lower()

# print("Bye")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is Not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Right your # is {num}")
