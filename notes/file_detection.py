# File Detection

import os

file_path = r"C:\Users\limas\Desktop\test"

if os.path.exists(file_path):
    print(f"The path '{file_path}' exists.")
    if os.path.isfile(file_path):
        print(f"The path '{file_path}' is a regular file.")
    elif os.path.isdir(file_path):
        print(f"The path '{file_path}' is a directory.")
else:
    print(f"The path '{file_path}' does not exist.")