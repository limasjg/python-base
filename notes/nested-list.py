# This is a nested list
my_list = [["item1", "item2"], ["item3", "item4"]] 

# Accessing an element in the nested list
# Access the element at row 1, column 0
# element = my_list[1][0]

# print(element)

for element in my_list:
    for item in element:
        print(item, end=" ")