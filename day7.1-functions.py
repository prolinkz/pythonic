### Functions & Limbda Functions in Python

## What is Function?
# A function is a block of code which only runs when it's called.
# You can pass data, known as *arguments* or parameters, into a function. 
# The function may perform some calculations or operations on this data.
# A function can also 
# Return data as a result.
# In Python, a function is defined using the def keyword.


# - [ ] **Functions**
# - [x] Basic function definition and calling
# - [x] Function with parameters and return values
#     - [x] Nested functions (functions within a function)
#     - [x] Variable scope, global vs local variables.
# - [x] Default parameter value
# - [x] Keyword arguments for more flexibility when passing multiple argument to the same function call
#     - [x] Arbitrary number of keyword arguments using `*args` syntax
# - [x] Using `**kwargs` syntax to pass dictionary as an argument
# - [x] Lambda functions: small anonymous functions that are defined on the fly
# - [x] Recursion: defining a function that calls itself


# Declare function with keyword def, function name will greet_user. 
# Call the function to return the value.
def greet_user():
    print("Hello, User!")
    greet_user() # Calling the function


def aoa():
    print("Asalam O aaliakum, All from Pakistan")
    aoa()


# Use Parameter to print the value
def hello(name):
    print('hello'+ name )
    print(hello())
    greet_user()
    print(hello('Rahul'))
    print(hello('Ali', 'Sultan', 'Zia'))
    greet_user()


def salam(name):
    print(f"Asalam O Aliakum, {name}!, Kaifa Haluk?")
    salam('<NAME>')
    salam("<NAME>")
    salam('Muhammad Ali')
    
# Calling default value to the funtion
def ao(name = "banda"):     # calling default value to the function
    print(f"{name}, Bandar-e Asalam o alaikum.")
    print(ao()) # or 
    ao("Azam")


## How to use function to Return Values
# 1st way to call function and return value
def square(number):
    result = number * number
    return result
print(square(5))   # Output : 25

# 2nd way to call function and return value
def square(number):
    return number * number
print(square(5))   # Output : 25

# 3rd way to call function and return value 
def square(number):
    return number * number
result = square(5)
print(result)   # Output : 25


## Nested Functions
# Define a cube function and return it value
def cube(num1=30):
    def inner_cube(num2=4):
        # num1 is local variable
        # num2 is local and nonlocal variables
        num1 += num2
        num2 += num1
        return num1, num2
    return inner_cube()
print(cube())





## Recursion
# define factorial function
def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n - 1)
    print(facto(6))
    ## Closures
    # create closure for add function with parameter x as global scope
    x = "Global Variable"
    def add():
        x = 'Local Variable'
        add()    # Call the Function


## what is lambda function?
# Lambda functions are small anonymous functions. They can take any number of arguments but only one expression which has to be evaluated.
x = lambda a: a + 10
print(x(5)) # Output: 5+10 = 15

y = lambda b: b / 2
print(y(4)) # Output: 4/2 = 2

# Another lambda example for two values.
# Example
z = lambda x, y: x * y
print("Lambda Func:", z(2,8))

# Example 
lambda_func = lambda x, y: (x + y) / 2
print("Lambda Func:", lambda_func.__doc__)


# We also can define proper function as lambda
def x(a):
    return a/2
x= lambda a: a / 2
print(x(3))  # Output: 3/2=1.5

# Or define lambda funtion for two values a, b multiplication
def mult(a,b ):
    return a*b
mult= lambda a,b : a*b
print('Multiplication:', mult(7,9))   #Output: Multiplication: 63






## What are decorators in Python ?
def mydecorator(func):
    """This is docstring of decorator."""
    def wrapper(*args,**kwargs):
        """Wrapper Docstring."""



### ASSIGNMENT
# Define 10 default def and lambda functions

lambda x: x**2 
print(square(2)) 

def square(x): 
    return x**2 
print(square(2)) 

even= lambda x: x%2 
if even(5)==0: 
    print("Number is even") 
else: 
    print("number is odd")
    
def even(x): 
    return x%2 
if even(4)==0: 
    print("Number is even") 
else: 
    print("number is odd") 
    maximum= lambda x,y: x 
    if x>y: 
        print(maximum(2,4)) 


def maximum(x,y): 
    return x 
if x > y: 
        print("X is greater than Y") 
else:
    print(maximum(4,6)) 
uppercase= lambda x: x.upper() 
print(uppercase("abc")) 

def uppercase(x): 
    return x.upper() 
print(uppercase('def'))


# Program-1: Square of a Number 
square = lambda num : num ** 2 
print(square(8)) 

# Program-2: Find Maximum of Two Numbers using limbda function
max = lambda num1, num2 : num1 > num2
print(max(5, 10))


# Program-3: Compute Length of the String 
length = lambda str : len(str) 
print(length("Hi! My Name is Awais")) 

# Program-4: Calculate Area of Rectangle 
area = lambda width, length : length * width 
print(area(4, 5)) 

# Program-5: Calculte Area of Triangle 
triangle = lambda base, height : 0.5 * base * height 
print(triangle(4, 5)) 

# Program-6: Calculate Area of Circle 
circle = lambda radius : 3.14 * radius ** 2 
print(circle(5)) 

# Program-7: Calculate Volume of Cube 
cube = lambda side : (side ** 3) / 6 
print(cube(5)) 

# Program-8: Double Each Number in the List 
double_nums = lambda nums : [n * 2 for n in nums] 
print(double_nums([1, 2, 3, 4, 5])) 

# Program-9: Reverse a String 
rev = lambda str : str[::-1] 
print(rev("Hello World")) 

# Program-10: Power of a Number 
# power = lambda base, exp : 1
# if exp == 0 :
#  print()   
# else: 
#     base = power(base, exp - 1) 
#     print(power(2, 3))


