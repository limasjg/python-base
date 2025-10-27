# Format specifiers are flags that you can format some value like: {value:flags}

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 5.56452 
price2 = -458.00
price3 = 12.50

print(f"{price2:.2f}")
print(f"{price2:10}") # Show ten places
print(f"{price2:010}") # Show ten places with zero
print(f"{price2:<10}") # adjusts where the arrow point
print(f"{price2:^10}") # centralizes
print(f"{price1:+}") # Shows the signal

