# variable scope is where a variable is accessible in the code. There are 4 types of variable scope:
# 1. Local scope: variables defined inside a function, only accessible within that function.        
# 2. Enclosing scope: variables defined in the outer function, accessible in the inner function.
# 3. Global scope: variables defined at the top level of a module, accessible throughout the module.
# 4. Built-in scope: variables defined in the built-in namespace, accessible in any part of the code.
# The order of variable resolution is: Local -> Enclosing -> Global -> Built-in (LEGB rule).

# Example of variable scope
x = "Global variable"
def outer_function():
    x = "Enclosing variable"
    
    def inner_function():
        x = "Local variable"
        print(x) # Local variable will be printed
    
    inner_function()
    print(x) # Enclosing variable will be printed

outer_function()
print(x) # Global variable will be printed

import math
print(math.pi) # Built-in variable will be printed