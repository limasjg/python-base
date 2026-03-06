# List comprehension is a concise way to create lists in python.
# [expression for value in iterable if condition]

# Simple example
doubles = [x * 2 for x in range(1, 11)]
# print(doubles)


#String example
fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# With condition
numbers = [-1, -2, -3, 4, 5, 6]
positive_nums = [num for num in numbers if num >= 2]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

# print(odd_nums)