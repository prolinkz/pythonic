
### Exceptional handling or error handling on user wrong input value for the required datatype format data.
## user can input any value, so it the programmer responsibility to teach the machine that the data input by the User is not valid, and gave Error msg
# For Example, below the user is needed to inout the number but what if he input the string 
num1 = int(input("Enter your number hers: "))
print(num1 + 3)  # print user input value and plus + 3 to it
           # what if the user input the string value, it will give error
  # To control this issue, programmer need to handle it theough try and except:
try:
    num2 = int(input("Enter your number here: "))
    print(num2 + 3)   # it will print value input + 3, if it takes number value
except:
  print("Enter correct number in text box")   # Through Error message, if it recieve text string instead
  print("Thank You!")

## If you want to print the error type, we can use the Exception as e: function. Example
try:
  a = int(input("Enter your number here: "))
  print(a + 7)
except Exception as e:
  print("Some error Occured")



#### FILE I/O HANDLING
## TO Write or Read File

s = "Harry is a good boy"    # store this string in a file
with open("text.txt", "w") as f:
  f.write(s)

## Open txtet file to 
fp = open("text.txt", "w")
fp.write(s)
fp.close()

## Reading a file. we use "r" to read a file

with open("file.txt", "r") as f:
  s = f.read()
  print(s)

         
## https://www.youtube.com/watch?v=fqF9M92jzUo
# OOPS in Python


           
