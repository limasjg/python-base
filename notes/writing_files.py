# Python writing files (.txt, .json, .csv)

txt_data = "Hello, this is a sample text file.\nThis file is used to demonstrate writing files in Python."

file_path = r"C:\Users\limas\Desktop\example.txt"

with open(file_path, 'w') as file:
    file.write(txt_data)
    print(f"Data has been written to {file_path}")