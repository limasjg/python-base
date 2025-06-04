# Conditions expression is one-line for teh if-else statment (ternary operator)
# Print or assingn on of two values on a condition
# X if condition else Y

num = 9
a = 50
b = 10
age = 15
temperature = 5
role = "user"

#print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
max_num = "A" if a > b else "B"
min_num = "A" if a < b else "B"
status = "Adult" if age >= 18 else "Not adult"
weather = "Hot" if temperature > 20 else "Cold"
user_role = "Acess" if role == "Admin" else "Not Acess"

print(user_role)