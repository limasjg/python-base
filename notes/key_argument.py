# keyword argument is used when you need different positions 

def hello(greeting, tittle, name, last_name):
    print(f"{greeting} {tittle} {name} {last_name}")

# hello("Hello", last_name="Lima", name="John", tittle="Mr.")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

my_phone = get_phone(country=55, area=11, first=98765, last=4321)

print(my_phone)