# For loops are a block of code that you execute a fixed number of times.
# Can be used in strings, ranges, sequences, etc

# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1, 11)): # Invert
#     print(x)

# for x in range(1, 11, 2): # 2 is the reason
#     print(x)

# credit_card = "1234-5678-9121-3456"

# for num in credit_card:
#     print(num)

for x in range(1, 20):
    if x == 15 + 1:
        break
    else:
        print(f"{x:02d}")