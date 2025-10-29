# nested loops are loop within another loop (outer, inner)
#   outer loop:
#       inner loop:

# for x in range(3):
#     for y in range(0, 10):
#         print(y, end="")
#     print()

#Example:

rows = int(input("Enter a # of rows: "))
columns = int(input("Enter a # of columns: "))
symbol = input("Enter a Symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()