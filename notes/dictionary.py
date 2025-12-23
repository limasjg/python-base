# A collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"}

# print(capitals.get("Brazil"))

# if capitals.get("India"):
#     print("That Capital exists")
# else:
#     print("That Capital doesn't exist")

# capitals.update({"Brazil": "Brasilia"})
# capitals.update({"China": "Tokyo"})
# capitals.popitem()

# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()

# for value in capitals.values():
#     print(value)

item = capitals.items()

for key, value in capitals.items():
    print(f"{key}:{value}")