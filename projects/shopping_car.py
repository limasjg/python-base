# Shopping car

item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would you like? "))

total = quantity * price

print(f"Your total is {total:.2f}")