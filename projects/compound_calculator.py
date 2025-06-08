# Python compound interest calculator

principle = 0
rate = 0
time = 0
# principle = float(input("Enter the principle amount: "))
# rate = float(input("Enter the rate: "))
# time = int(input("Enter the time in years: "))


while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("The principle can't be lass than zero")
    else:
        break

while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("The rate can't be lass than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("The time can't be lass than zero")
    else:
        break
    
total = principle * pow((1 + rate / 100),time)

print(f"The total amount is {total:.2f}")