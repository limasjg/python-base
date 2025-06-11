# nested loop = A loop within another loop (outer, inner)
# outer loop:
#   inner loop:

# for x in range(3):
#     for y in range(0, 10):
#         print(y, end=" ")
#     print()

rows = int(input("Enter the # rows: "))
Columms = int(input("Enter the # Columns: "))
symbol =input("Enter the Symbols: ")

for x in range(Columms):
    for y in range(rows):
        print(symbol, end="")
    print()