# Decorator is a function that extends the behavior of another functions without modifying the original function's code.
# Decorators are often used for logging, access control, memoization, and other cross-cutting concerns.


def add_chocolate(func):
    def wrapper(*args, **kwargs):
        print("Adding chocolate ice cream...")
        func(*args, **kwargs)
    return wrapper

def add_vanilla(func):
    def wrapper(*args, **kwargs):
        print("Adding vanilla ice cream...")
        func(*args, **kwargs)
    return wrapper

@add_chocolate
@add_vanilla
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream!")

get_ice_cream("strawberry")  # Output: Here's your strawberry ice cream!