

print('''
      # What is Conda and Conda Environment?
      - Conda: its an IDE, a software that run the python programming 
      - Conda Environment/Container: it a place or room or box where we place all the softwares

    # Create Environment for Machine Learning named "python_ml"
      open conda command prompt
      (base) C:/user/Admin> conda env list  # show all environments
      (base) C:/user/Admin> conda create -n python_ml   # create new environment
      (base) C:/user/Admin> conda activate python_ml    # Enter into python_ml env
      (python_ml) C:/user/Admin> conda list
      (python_ml) C:/user/Admin> conda install python
      we also can install python with specific version, like python=3.09
      (python_ml) C:/user/Admin> conda install python=3.09
      (python_ml) C:/user/Admin> conda list
      (python_ml) C:/user/Admin> conda deactivate   # it willl return to (base) environment.

      
      ''')

print('''
      If we create an Environment along with installion of python within that environment, we will type
      # Create python_dl environment for Deep Learning.
      (base) C:/user/Admin> conda create -n python_dl python=3.11
      
      # search/list environments
      (base) C:/user/Admin> conda env list

      # Enter into python_dl environment
      (base) C:/user/Admin> conda activate python_dl

      # List all installed softwares
      (python_dl) C:/user/Admin> conda list

      # Out from the existing/activated environment, and direct to (base) root environment
      (python_ml) C:/user/Admin> conda deactivate

      # To remove/delete the environment, suppose delete python_ml environment.
      (base) C:/user/Admin> conda env remove --name python_ml

      
      ''')

# Assignment Day5: 
print('''
      * Python Libraries:
      Python is a versatile programming language with a rich ecosystem of 
      libraries and frameworks that cater to a wide range of applications and domains. 
      Here are some of the most commonly used libraries in Python: 
      1. NumPy: A fundamental library for scientific computing with support for large, 
        multi-dimensional arrays and matrices, along with a collection of mathematical functions. 
        (Numpy is a Python library that allows you to do mathematical calculations very easily. 
        It has many functions that allow you to perform these calculations.)
      2. pandas: Provides data structures and data analysis tools for handling and manipulating 
        structured data, such as data frames and time series. 
        (With pandas, you can quickly read in data from a variety of sources, including CSV, Excel, and SQL databases. 
        You can then use pandas to manipulate and transform your data, as well as to create useful visualizations, such as bar and line charts)
      3. Matplotlib: A popular 2D plotting library for creating static, animated, or interactive visualizations in Python. 
        (One way to use plots in Visual Studio Code is with Juypiter notebooks , it’s useful to grasp the core concepts of matplotlib’s design)
      4. Seaborn: Built on top of Matplotlib, Seaborn offers a high-level interface for creating informative and attractive statistical graphics. 
        (Seaborn is a library for making statistical graphics in Python. It builds on top of matplotlib and integrates closely with pandas data structures. 
        Seaborn helps you explore and understand your data)
      5. Scikit-learn: A powerful library for machine learning and data mining, containing various algorithms for classification, regression, clustering, dimensionality reduction, and more. 
        (regression, clustering, and dimensionality reduction)
      6. TensorFlow and PyTorch: These deep learning frameworks are used for building and training neural networks for tasks like image recognition, natural language processing, and more. 
      7. Keras: Often used in conjunction with TensorFlow or PyTorch, Keras provides a high-level API for building and training neural networks. 
      8.SciPy: Extends the capabilities of NumPy by adding additional functionality for optimization, integration, interpolation, eigenvalue problems, and more. 
        ( It can operate an array of NumPy libraries and has also optimized the functions used in NumPy)
      9. NLTK (Natural Language Toolkit): A library for working with human language data, including text analysis, tokenization, stemming, and various natural language processing (NLP) tasks. 
      10. Flask and Django: Web frameworks for building web applications in Python. Flask is minimalistic and micro, while Django is a full-stack framework with many built-in features.

      ''')

      ## VARIABLES
m = "We are learners" # String
n = 3   # Integer
o= 3.2 # Float 


      # OPERATORS
      # 
print('''
            
    # Assign Operators
          x = y
          x = 3
          x = "We are programmer"

          print(x)
          
          
    # Arithimatic Operators
     
            print( x + y)
            print(x - y)
            print(x * y)
            print(x / y)
            print(x % y)

    # Comparission Operators
            print(x > y)
            print(x < y)
            print(x == y)
            print(x != y)
            print(x && y)
            print(x || y)
      


''')

## Comparision Operators 
a = 5
b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)



## Logical Operators

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

# Example
a = 5
b = 6

print((a > 2) and (b >= 6))    # True




## Data Types

n = 5   # Integers
y = 5.0     # Float
z = "Asalam O Alaikum, "    # String
a = [1, 2, 3]   # List of Integers
a_1 = ["Usama", "Laiaba", "Sanam", "Irum"]    # Liast of Strings
b = (1, 2, 3)   #tuple

c = {"Usama":5, "Laiba":5.2, "Irum":6.0}   # Dictionary "key":value
d= {1,2,3}  # Set



## CONDITIONAL STATEMENTS
if True:
  print("This is true!")
else: 
   print("This is false.")
    

## IF -Else
    
x = int(input("Enter x:"))
y = input("Enter y:")
if x > 5 and len(y)>4:
  print("x is greater than five and length of string y is more than four characters.")
else:
  print("Either condition is False")
  


####  Another Example  
x = 4
y = 7
if x < y:
  print("x is smaller than y.")
else:
  print("x is not smaller than y.")


## LOOPING STRUCTURES
for i in "Hello World":           ## Iterating through each character present inside Hello world String
  for i in range(6):
    print(i**2)
    break


## Nested Loops

for num in range(1, 9):
  if num % 2 == 0:
    continue
  else:
    print(num)
    # FLOW CONTROL STATEMENTS
    break


# NESTED FOR-LOOP
  for j in range(1, 8):
    if (j+1)%2==0:
      continue
    else:
      print(f"{num} * {j} = {num*j}")
      break


# Another Example
for i in range(5):
    print(i)
    while True:
        break


## Functions
def myFunction():
  return "Hello World!"
    
