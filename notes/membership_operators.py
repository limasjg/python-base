# Membership operators are used to test if a value is found in a sequence (string, list, tuple, set and dictionary).
# The operators are: in and not in

# word = "Python"

# letter = input("Guess a letter: ")

# if letter in word: # You can use not in to check if the letter is not in the word
#     print(f"'{letter}' is in the word '{word}'")
# else:
#     print(f"'{letter}' is NOT in the word '{word}'")




#Dictionary Example

# grades = {"john": "A", 
#           "alice": "B", 
#           "bob": "C"}

# student_name = input("Enter a student name: ")

# if student_name in grades:
#     print(f"{student_name} has a grade of {grades[student_name]}")
# else:
#     print(f"{student_name} is not found in the grades dictionary.")

email = "user@gmail.com"

if "@" and "." in email:
    print("Valid email")
else:    
    print("Invalid email")