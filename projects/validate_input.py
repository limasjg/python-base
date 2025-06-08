# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12 or  " " in username or any(char.isdigit() for char in username):
    print("Invalid username. Please ensure it is no more than 12 characters, contains no spaces, and has no digits.")
else:
    print("Valid username.")