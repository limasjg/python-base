# Weight converter program

weight = float(input("Enter your wight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight in Pounds is {weight:.1f}{unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight in Kilograms is {weight:.1f}{unit}")

else:
    print(f"{unit} not valid")

# best way to do:

# while True:
#     try:
#         weight = float(input("Enter your weight: "))
#         break
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número válido para o peso.")

# unit = input("Kilograms or Pounds? (K or L): ").strip().upper()

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight in Pounds is {weight:.1f} {unit}")

# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight in Kilograms is {weight:.1f} {unit}")

# else:
#     print(f"{unit} is not a valid unit.")
