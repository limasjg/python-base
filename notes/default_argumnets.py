# A default value for certain parameters, used when it is omitted, make your function more flexible.
# Can be 1.Position, 2.Default, 3. keyword, 4.arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500,  0.2, 0))