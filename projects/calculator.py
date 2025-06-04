# Caculator program

operator = input(" Enter a operator (+, -, * or /): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2sd number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result is {result:.2f}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is {result:.2f}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is {result:.2f}")
elif operator == "/":
    result = num1 / num2
    print(f"The result is {result:.2f}")
else:
    print("The operator is invalid")
