# Validate user input exercise
# 1. username is more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Enter your name: ")

# if len(name) > 12 or " " in name or not name.isalpha():
#     print("Invalid name")
# else:
#     print(f"Welcome {name}")

# print("Invalid name" if len(name) > 12 or not name.isalpha() else f"Welcome {name}")

if len(name) > 12:
    print("You have more than 12 characters")
elif not name.find(" ") == -1:
    print("Your string has spaces.")
elif not name.isalpha():
    print("You cant use number")
else:
    print(f"Welcome {name}")