# Python writing files (.txt, .json, .csv)


##################################.TXT FILES ###############################
# txt_data = "Hello, this is a sample text file.\nThis file is used to demonstrate writing files in Python."

# file_path = r"C:\Users\limas\Desktop\example.txt"

# try:
#     with open(file_path, 'a') as file:
#         file.write("\n" + txt_data)
#         print(f"the file in {file_path} was created")

# except FileExistsError:
#         print(f"The file {file_path} already exists.")

# fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# file_path = r"C:\Users\limas\Desktop\example.txt"

# try:
#     with open(file_path, 'w') as file:
#         for fruit in fruits:
#             file.write("\n" + fruit)
#         print(f"the file in {file_path} was created")

# except FileExistsError:
#         print(f"The file {file_path} already exists.")




##################################.JSON FILES ###############################

# import json

# employees = {
#     "employees": [
#         {"name": "Alice", "age": 30, "department": "HR"},
#         {"name": "Bob", "age": 25, "department": "Engineering"},
#         {"name": "Charlie", "age": 35, "department": "Sales"}
#     ]
# }

# file_path = r"C:\Users\limas\Desktop\example.json"

# try:
#     with open(file_path, 'w') as file:
#         json.dump(employees, file, indent=4)
#         print(f"the file in {file_path} was created")

# except FileExistsError:
#         print(f"The file {file_path} already exists.")

##################################.CSV FILES ###############################

import csv

employees = [["Name", "Age", "Department"],
             ["Alice", 30, "HR"],
             ["Bob", 25, "Engineering"],
             ["Charlie", 35, "Sales"]]

file_path = r"C:\Users\limas\Desktop\example.csv"

try:
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';') 
        writer.writerows(employees)
        print(f"the file {file_path} was created")

except Exception as e:
    print(f"Error: {e}")

