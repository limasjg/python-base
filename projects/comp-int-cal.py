# Crate a principal interest calculator

principal = 0
rate = 0
time = 0 # Years

# while principal <= 0:
#     principal = float(input("Enter the principal amount: "))
#     if principal <= 0:
#         print("Principal can't be lass than or equal a zero.")

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be lass than or equal a zero.")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("time can't be lass than or equal a zero.")

# total = principal * pow((1 + rate / 100), time)
# print(f"Your balance after {time} year/s: ${total:.2f}")

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than zero.")
    break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time can't be less than zero.")
    break
        

total = principal * pow((1 + rate / 100), time)
print(f"Your balance after {time} year/s: ${total:.2f}")