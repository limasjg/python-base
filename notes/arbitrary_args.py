# def add(x, z):
#     return x + z
 
# Args you can pass multiple non-key arguments
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1, 1, 9))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_address(street="street number one", 
#               city="SP", 
#               zip="11222-550", 
#               apt="100")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Dr.", "Strange",
              city="SP", 
              zip="11222-550", 
              apt="100")

