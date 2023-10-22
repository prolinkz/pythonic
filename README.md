# pythonic - Python Startup

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

### Python file extensions
- To save a file in Python format, a <code> .py </code> extension will used.
- To save a Python Notebook file, the file extension wiould be used <code> .pynb </code> where we can write code and document it metadata at single file.
- Hash (#) is used in Python for a comment.

## Python Data Types
### String's

- Double quotation <code> print("Hello") </code>
- single quotation <code> print('Learn Python') </code>
- Multi line quotation <code>   print(''' Multiline String - using Tripple quotations ''' )   </code>

## Opertor's

- Addition                     <code> print(2+5) </code>
- Substration                  <code> print(2-5) </code>
- Division Float               <code>   print(6/2)   </code> #Output will be 3.0
- Division Int                 <code>   print(6//2)   </code> #Output will be 3
- Remainder, after division    <code> print(13%2) </code>
- Exponent/Power               <code> print(2**6) </code> i-e: 2x2x2x2x2

 #### PEMDAS Rule - Paranthesis, Exponent, Multiplication, Division, Addidtion, Substraction (Python use this model)
 #### BODMAS Rule - Bracket, Order/Power, Division, Multiplication, Addidtion, Substraction
 

## How To Add (+) 2 digits or variable values in Python

Add (+) 2 digits or variable values in Python using the following code:
- Declare the variables,a assign values to them
<code> num1 = 5, </code>
<code> num2 = 10 </code>

- Sum both the declared variable using + operator
<code> sum = num1 + num2 </code>

- Print the result
<code> print("The sum of the two numbers is:", sum) </code>


```
num1 = 5
num2 = 10

sum = num1 + num2

print("The sum of the two numbers is:", sum)

```

```
num1= 5
num2 = 10
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")
```

```
name="John" #This is a string data type
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")
```

```
# The sum of 5 and 10 is 15

print(f"The product of {num1} and {num2} is {num1 * num2}")
```


<p></p>

<p>In this code, we define two variables `num1` and `num2` and assign them the values 5 and 10, respectively. We then add the values of these variables and store the result in a new variable called `sum`. Finally, we print the result.</p>

<p>You can replace the values of `num1` and `num2` with any two digits or variables you want to add. The code will work the same way.</p>


<p></p>


## String Statements are in Pythons
<p>
 <b> 1. String Literals:</b> These are sequences of characters enclosed in matching single quotes (') or double quotes ("). For example, 'Hello, World!' and "Hello, World!" are both string literals.

 <b> 2. String Concatenation:</b> This is the process of combining two or more strings into a single string. In Python, you can concatenate strings using the '+' operator. For example, 'Hello, ' + 'World!' results in the string 'Hello, World!'.
 ```
# Use + sign to join strings and variables.
name="John" #This is a string data type
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")
# Output: My name is John and I am 30 years old.
```

<b> 3. String Interpolation:</b> This is a way to embed expressions inside string literals. In Python, you can use f-strings (formatted string literals) to achieve this. For example, f'The sum of {num1} and {num2} is {sum}' results in the string 'The sum of 5 and 10 is 15'.
```
#Use Curly Brace {} to hold the variable value within a string.
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is John and I am 30 years old.
```

<b>4. String Multiplication:</b> This is the process of <emp>repeating a string</emp> a specified number of times. In Python, you can use the '*' operator to multiply strings. For example, 'Hello, ' * 3 results in the string 'Hello, Hello, Hello, '.

<b>5. String Slicing:</b> This is a way to extract a portion of a string. In Python, you can use <emp>slicing</emp> to achieve this. For example, 'Hello, World!'[0:5] results in the string 'Hello'.

<b>6. String Methods:</b> Python provides a set of built-in methods for strings. For example, len('Hello, World!') returns the <emp>length of the string</emp>, which is 13.

<b>7. String Formatting:</b> This is a way to format strings using placeholders. In Python, you can use the <emp>str.format() method or f-strings</emp> to achieve this. For example, 'The sum of {} and {} is {}'. format(num1, num2, sum) results in the string 'The sum of 5 and 10 is 15'.

<b>8. String Escaping:</b> This is a way to <emp>include special characters</emp> in a string. In Python, you can use <emp>escape characters</emp> to achieve this. For example, 'Hello, \nWorld!' results in the string 'Hello, ' followed by a __newline character__ and then the string 'World!'.

<b>9. String Strip:</b> This is a way to remove leading and trailing characters from a string. In Python, you can use the str.strip() method to achieve this. For example
</p>



  

