# Num pad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (5, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()  # Print a new line after printing all items in the row