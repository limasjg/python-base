# You can use the logical operators to evaluate multiple conditions with OR, AND and NOT

temp = 30
is_sunny = False

if temp >= 30 and is_sunny:
    print("Its hot outside 🥵")
    print("It's sunny ☀️")
elif temp <= 0 and is_sunny:
    print("Its cold outside 🥶")
    print("It's sunny ☀️")   
elif 30 > temp > 0 and is_sunny:
    print("Its cold warm 😊")
    print("It's sunny ☀️") 
elif temp >= 30 and not is_sunny:
    print("Its hot outside 🥵")
    print("It's cloud ☁️")
elif temp <= 0 and  not is_sunny:
    print("Its cold outside 🥶")
    print("It's cloud ☁️")   
elif 30 > temp > 0 and not is_sunny:
    print("Its cold warm 😊")
    print("It's cloud ☁️") 