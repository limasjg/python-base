# Collection = Single "Variable" used to store multiple values
# List = Ordered and changeable. Duplicates are allowed.
# Set = unordered and unindexed. No duplicate members. But add/remove is allowed.
# tuple = Ordered and unchangeable. Duplicates are allowed. Faster


# List
fruits = ["apple", "banana", "cherry", "orange"]
# print(dir(fruits))  # List of methods and attributes of the list object
# print(fruits[4])  # Accessing the first element of the list
#print(len(fruits))  # Length of the list
#print("apple" in fruits)  # Check if "apple" is in the list
# fruits.append("kiwi")  # Adding an item to the end of the list

# for fruit in fruits:

#print(fruits)

# Set
fruits_set = {"apple", "banana", "cherry", "orange"}

# fruits_set.add("kiwi")  # Adding an item to the set
# fruits_set.remove("banana")  # Removing an item from the set
print(fruits_set)  # Print the set

#Tuple
fruits_tuple = ("apple", "banana", "cherry", "orange")
# fruits_tuple[0] = "kiwi"  # This will raise an error because tuples are immutable
# fruits_tuple = fruits_tuple + ("kiwi",)  # This will create a new tuple
print(fruits_tuple)  # Print the tuple