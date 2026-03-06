# if __name__ == "__main__": (this script can be imported OR run directly)
# Functions and classes in this module can be reused without the main block of code executing.
# Good practice (code is modular, helps readability, leaves no global variables and avoid unintended executions)

# example of main block of code

def greeting(name):
    print(f"Hello, {name}!")

def add(x, y):
    total = x + y
    print(total)

def main():
    pass    

if __name__ == "__main__":
    main()