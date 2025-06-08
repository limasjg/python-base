# format specifiers = {value:flags} format a value based on the flags
# flags = {width} {precision} {type}

# . (number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

value1 = 1234567.89123456789
value2 = 1234567.89123456789

print(f"{value1:.2f}")  # Fixed point with 2 decimal places
print(f"{value1:,.2f}")  # Comma separator with 2 decimal places
print(f"{value1:>20.2f}")  # Right justify in 20 spaces with 2 decimal places
print(f"{value1:<20.2f}")  # Left justify in 20 spaces with 2 decimal places
print(f"{value1:^20.2f}")  # Center align in 20 spaces with 2 decimal places
print(f"{value1:+.2f}")  # Plus sign for positive value with 2 decimal places
print(f"{value1:=.2f}")  # Sign to leftmost position with 2 decimal places
print(f"{value1: 20.2f}")  # Space before positive numbers with 2 decimal places
print(f"{value1:03.2f}")  # Zero pad to 3 spaces with 2 decimal places
