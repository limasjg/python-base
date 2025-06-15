# Concession stand program

menu = {
    "popcorn": 5.00,
    "soda": 3.00,
    "candy": 2.50,
    "nachos": 4.00,
    "hot dog": 6.00,
    "pretzel": 3.50,
    "ice cream": 4.50,
    "chips": 2.00,
    "water": 1.50,
    "coffee": 2.50
}

cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")    


while True:
    food = input("Enter an item to add to your cart (or 'q' to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)
for item in cart:
    print(item, end=" ")

print()  # Print a newline for better formatting
print(f"Your total is: ${total:.2f}")