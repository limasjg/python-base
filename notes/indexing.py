# indexing = Accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_card = "1234-5678-9012-3456"

# print(credit_card[0])
# print(credit_card[:4])
# print(credit_card[6:9]) 
# print(credit_card[:3])
# print(credit_card[-1])
# print(credit_card[::2]) # Output: 1234-

# print(credit_card[-4:])

# last_four_digits = credit_card[-4:]
# print(f"XXXX-XXXX-XXXX-{last_four_digits}")

credit_card = credit_card[::-1]

print(credit_card)