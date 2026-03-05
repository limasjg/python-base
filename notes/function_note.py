# Function is a block of reusable code
# place () after the function name to invoke it.

def happy_birthday(name, age):
    print(f"Happy birthday to {name} for your {age} years old!")

# happy_birthday("João", 33)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}, your bill of ${amount:.2f} is due: {due_date}.")

# display_invoice("Caloteiro", 5000.564, "10/03")

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def mult(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

# print(div(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("joão", "lima")
print(full_name)