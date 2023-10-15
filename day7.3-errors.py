print('''
what are types of errors in python, and how to deal with each. Explian with example.

Blackbox AI
Errors in Python can be broadly classified into two categories: syntax errors and runtime errors.

- Syntax errors occur when the code is incorrect according to the Python syntax rules. These errors are detected by the Python interpreter before the code is executed. For example, if you forget to include a colon at the end of a statement, you will get a syntax error.

To deal with syntax errors, you need to carefully review your code and fix the errors. You can use the Python debugger to help you find and fix syntax errors.

- Runtime errors occur when the code is syntactically correct, but an error occurs when the code is executed. These errors are detected by the Python interpreter during the execution of the code. For example, if you try to divide a number by zero, you will get a runtime error.

To deal with runtime errors, you need to use exception handling. Exception handling allows you to catch and handle runtime errors so that your program can continue to run. For example, you can use the try-except statement to catch and handle a ZeroDivisionError.

Here is an example of how to deal with a runtime error using exception handling:
      
      ''')

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result is", result)
finally:
    print("This block will always execute")

# This code will catch the ZeroDivisionError and print a message to the user. The program will then continue to run.

## TYPES OF ERROR'S
- SyntaxError
# Syntax errors occur when the parser encounters invalid code. This includes things like missing or mismatched brackets, incorrect indentation levels, unexpected tokens (
- NameError
- TypeError
- ValueError
- IndexError
- KeyError
- AttributeError
- ImportError
- ModuleNotFoundError
- ZeroDivisionError
- FileNotFoundError
- FileExistsError
- AssertionError
- MemoryError
- SystemExit
- EOFError
- OSError
- IOError
- WindowsError
- EnvironmentError
- NotImplementedError
- RecursionError

