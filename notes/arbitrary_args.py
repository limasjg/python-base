# def add(x, z):
#     return x + z

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 1, 9))