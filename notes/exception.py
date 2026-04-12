# Exception and event that interrupt the normal flow of the program.
# (ZeroDivisionError, TypeError, ValueError, etc.)
# 1.try, 2.except, 3.finally

#try:
#    # Code that may raise an exception
#except Exception:
#    # Code to handle the exception
#finally:
#    # Code that will always execute, regardless of whether an exception occurred or not

try:
    number = int(input("Enter a number: "))
    print(1 / number)

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")

except Exception:
    print("An unexpected error occurred.")

finally:
    print("This block will always execute, regardless of exceptions.")
    