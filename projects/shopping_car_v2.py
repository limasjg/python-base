# Shopping car v2

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (or 'q' to quit): ").lower()
    if food == 'q':
        break
    else:
        price = float(input(f"What is the price of {food}? "))
        foods.append(food)
        prices.append(price)
print("----------Your Shopping List----------")
for food in foods:
    print(food, end=" / ")

for price in prices:
    total += price

print()
print(f"Your total is {total:.2f}")
# Print the total price
print("Thank you for shopping with us!")