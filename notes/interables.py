# Iterables are objects that can be iterated over, meaning you can loop through them using a for loop or other iteration methods.
# Examples of iterables include lists, tuples, strings, dictionaries, and sets.

# ======== LISTS ========
print("=== LISTS ===")
fruits = ["apple", "banana", "cherry", "date"]
print("List:", fruits)

for fruit in fruits:
    print(f"  - {fruit}")

# List with mixed types
mixed_list = [1, "hello", 3.14, True]
for item in mixed_list:
    print(f"  Item: {item} (Type: {type(item).__name__})")


# ======== TUPLES ========
print("\n=== TUPLES ===")
coordinates = (10, 20, 30)
print("Tuple:", coordinates)

for coord in coordinates:
    print(f"  - {coord}")

# Tuple with mixed types
person = ("John", 25, "Engineer")
for data in person:
    print(f"  Data: {data}")


# ======== SETS ========
print("\n=== SETS ===")
colors = {"red", "blue", "green", "yellow"}
print("Set:", colors)

for color in colors:
    print(f"  - {color}")

# Set with numbers
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    print(f"  Number: {num}")


# ======== DICTIONARIES ========
print("\n=== DICTIONARIES ===")
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "city": "New York"
}
print("Dictionary:", student)

# Iterate over keys
print("Keys:")
for key in student:
    print(f"  - {key}")

# Iterate over values
print("Values:")
for value in student.values():
    print(f"  - {value}")

# Iterate over key-value pairs
print("Key-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary with different value types
config = {
    "timeout": 30,
    "enabled": True,
    "name": "MyApp",
    "version": 1.5
}
print("\nConfig Dictionary:")
for key, value in config.items():
    print(f"  {key}: {value} (Type: {type(value).__name__})")