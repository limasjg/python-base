# Nested list = A list that contains other lists as its elements
# Example of a nested list
nested_list = [
    ["apple", "banana", "cherry"],
    ["orange", "kiwi", "grape"],
    ["mango", "pineapple", "peach"]
]
# Accessing elements in a nested list
# print(nested_list)  # Accessing the first sublist
# print(nested_list[1][2])  # Accessing the third element of the second sublist

for list in nested_list:
    for item in list:
        print(item, end=" / ")
    print()  # Print a new line after printing all items