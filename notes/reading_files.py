# Reading Files

# TXT FILE
# file_path = r"C:\Users\limas\Desktop\example.txt"


# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print(content)
# except Exception as e:
#     print(f"An error occurred: {e}")

# JSON FILE
# import json

# file_path = r"C:\Users\limas\Desktop\example.json"

# try:
#     with open(file_path, 'r') as file:
#         content = json.load(file)
#         print(content["employees"][1]["name"])
# except Exception as e:
#     print(f"An error occurred: {e}")

# CSV FILE

import csv

file_path = r"C:\Users\limas\Desktop\example.csv"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = csv.reader(file, delimiter=';')
        for line in content:
            print(line[1])
except Exception as e:
    print(f"An error occurred: {e}")
