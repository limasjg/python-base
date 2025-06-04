# Logical operators evaluare multiple conditions (or, and , not)
# Or at least one condition must be true.
# And all of conditions must be true
# inverts the condition (not False, not True)

# OR
# temp = 20
# is_ranning = False

# if temp > 35 or temp < 0 or is_ranning:
#     print("The event will be canceled")
# else:
#     print("The event will be happen ")


# AND and NOT
temp = 10
is_sunny = False

if temp > 30 and is_sunny:
    print("It is Hot")
    print("It is Sunny")

if temp < 15 and is_sunny:
    print("It is Cold")
    print("It is Sunny")

if 30 >= temp >= 15 and is_sunny:
    print("It is OK")
    print("It is Sunny")

if temp > 30 and not is_sunny:
    print("It is Hot")
    print("It is Cloudy")

if temp < 15 and not is_sunny:
    print("It is Cold")
    print("It is Cloudy")

if 30 >= temp >= 15 and not is_sunny:
    print("It is OK")
    print("It is Cloudy")    