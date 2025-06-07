# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12 or " " in username or any(char.isdigit() for char in username):
    print("Username can't be bigger than 12 caracteres or have spaces or digits")
else:
    print(f"{username} created")    