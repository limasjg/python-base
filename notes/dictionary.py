# Dictionary = A collection of {key:value} pairs ordened and changeble. No duplicates.

capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Canada": "Ottawa"
}
print(capitals)  # Print the dictionary

for key, value in capitals.items():
    print(f"The capital of {key} is {value}")  # Print each key-value pair

# Adding a new key-value pair
capitals["Australia"] = "Canberra"
print("\nAfter adding Australia:")
print(capitals)  # Print the updated dictionary
# Removing a key-value pair
del capitals["Germany"]
print("\nAfter removing Germany:")