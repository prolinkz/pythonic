### Indentation and IF Condition

from unittest import case


a = 5
b = 15
c = 20.5

print (a < b)  # the output will be True

if a < b:
    print(" a is less then b")

# Another Example
print( c < b)

if c < b:
    print("c chota h b sy")  # the answer will be No/False, so we add else
else:
    print("c bara h b sy, pagly!")



### User Input program

name = input("Enter your name")     # input from user
# print(name)   #output
print("Hello", name, ", or snao k sy ho?")  # Output 


# Assignment age calculation of person_A and person_B.

person_A_name = input("Enter person A name: ")
person_A_age = input("Enter person A age: ")

person_B_name = input("Enter person A name: ")
person_B_age = input("Enter person A age: ")

if person_A_age > person_B_age:
    print(person_A_age, "is older then ", person_B_age)
else:
    print(person_A_age, "is younger then", person_B_age)


# To prevevent from Type Casting error while in fload input, use Int() function to output result in integer value.
person_A_age = int(input("Enter person A age: ")) 

# Or for Float
weight = float(input("Enter your wieght: "))



### DATA STRUCTURE and Indexing in PYTHON
# A data structure is a way of organizing and storing data in a computer system. 
# It defines the format and organization of data elements, as well as the operations that can be performed on them. 
# Data structures are designed to facilitate efficient data manipulation, retrieval, and storage.

## LIST

food = ["Dahi Bhalay", "Chicken Karai", "Samosa Chart", "Daal Rice", "Biryani"]
print("\n Food List : \t\t" , food )    ## Printing list

# Or simply 
print(food)     # this will print all the list elements (food items)
# Accessing a particular element in list using index number
print ("First Element=" + str(food[0]))   # Indexing starts at 0
print ("Second Element="+str(food [1])+" is my favourite.")      ### Note that indexing ends with -1 not to include last
print ("Second Element=", food[1])       # Second item is accessed by passing second argument as '1' to indexing function
print ("Second Element=" + str(food[1]) )   
print ("Third Element= "+str(food [2] ))      ### Note that here indexing is starting with zero not one!
print ("Fourth Element="+str(food[-4]))       #### Negative indexes are also allowed to access an item from right side
print ("Last Element="+str(food[-1]))         # -1 refers to last item in list

# We can also change the list item, like to change the last item of a list 'Biryani' to 'Pulao'
food[-1]='Pulao'
print('\n Modified List:'+str(food))        #### This prints modified list after changing an item value
# Adding new item into existing list by appending it's value as shown below
food.append('Roti')                          #### After modifying list we added another item named Roti
print ('\n Newly appended Item='+str(food [-1]))       ##### Here I am accessing last item which was just added
print ('Added New Item In Existing List:',food)       ##### Now printing updated list again
# Removing any specific item from list based on its position or index no., which you want ot remove
del food[3]                                #### Here we removed Dal Rice from our food list
print ('After Deletion Of One Item From The List: ',food)#### Now printing updated list again
# Sorting Lists
food.sort()                               #### Sorts alphabetically ascending order
print ('Sorted List:',food)              #### Now printing sorted list
# Reverse sorting lists
food.reverse()                           #### Changes the order of list elements
print ('Reversed Sorted List:',food)            #### Now printing reversed sorted list


## LIST COMPREHENSIONS
numbers=[num for num in range(1,10)]   ## This will create a list from 1 to 9
print("List Comprehension: ", numbers)

evenNumbers= [num*2 for num in range(1,10)]     ### Will multiply each number by two using list comprehensions
evenNumbers= [num*2 for num in range(1,10)]     ### This will generate even number upto nine
print('Even Numbers: ',evenNumbers)



## TUPLES
coordenate = (4.29, 92.40)
print(coordenate)       # Output (4.29, 92.40)
print(coordenate[0])    # Output (4.29)
 
 # Another Tupple Example
tup=(5,'Hello',True,[4,"Raju"])          ########### Tuple consists of immutable objects and are enclosed within parentheses ()

# Tuple are similar to list but they cannot be changed once created and they have fixed length i.e immutable
tuple_list=(5,'Hello',True,[4,"Hi"])          ########### tuple contains different data types
print(type(tuple_list),"\n")                 ############# type function returns datatype of variable

for x in range(len(tuple_list)):
    print(x,"\t:",tuple_list[x],end="\n\n")
 
    

## TUPLE
# Tuple are similar as lists but they cannot be changed once created unlike Lists.
# They use parenthesis () instead square brackets [] .
student = ("John Doe", 35, "Computer Science")
print("\n Student tuple : \t\t" , student )

## SET
fruits = {"Apple","Mango","Kiwi"}          # Creating set
print('\n Fruits Set:\t', fruits,"\n")       ####### Note that there is no order in sets
    # Add new item to the Set.
fruits.add('orange')

## DICTIONARY
# Dictionaries store data values in key-value pairs.
person = {'Name': 'Zara', 'Age': 7, 'Class':'6th'}
print ('Person Dictionary:', person,'\n')


# DICTIONARY OR HASHMAP IN PYTHON
Cars = {'brand':'Ford', 'Model':'Mustang', 'Year':1964}
print(Cars)
print(Cars['brand'])

# Change manufactoring year to 2023
Cars['Year'] = 2023
print(Cars) # Output all keys and values, or
print(Cars['Year']) # print only Year value for it key 'Year'

# Dalete Carr Model
del Cars['model']
print(Cars)




dict={'name':'<NAME>','Age':67}           ############### dictionary has key-value pairs
dict['Name']='Rajesh'                     ############## Updating values in Dictionary
print(dict["name"], "\t","is", "\t", dict["Age"], "Years Old.")
print(dict["Name"], "\t","lives", "\t", dict["Age"], "Years Ago.")
del dict['Age']  ######### deleting key Age


# ACCESSING VALUES
print('Accessing Values:')
print('Name:',person['Name'])        # Output: Zara
print('Age:',person ['Age'] )           ##### Note that we need to put space between Name and Age
#### If we write it like this without space then Python will consider it as one word i.e., NameAge
print('Class:',person ['Class' ] )      # Output: 6th

## ASSIGNENT
# 1- LIST: Elements in the list are in a specific order meaning you can call elements according to their index (i.e position). 
#   We can also make changes in our list (i.e. mutable). The list also contains a duplicate element. 
#   We can also do slicing in the list using index values. The list can be recognized by [] square brackets. 
# 2- TUPLE: Tuples are the data types that are immutable and that we cannot make changes in it. 
#   Its elements are in order and they also contain duplicate value. Tuple can be accessed by an index value. 
#   For tuples, we use () parenthesis. 
# 3- SET: set are mutable but their element are not in order so we cannot access them. 
#   It does not contain a duplicate value. for sets we use {} curly brackets. 
# 4- DICTIONARY: It consists of key: value pair, they are mutable. They do not maintain the order of items. 
#   Keys in a dictionary are unique, and they must be immutable (strings, numbers, or tuples typically). 
#   Values associated with keys can be of any data type. syntax of the dictionary is dic={"name":"Ali"}


### Control Flow Statement in Python
# what are Control Flow Statements in python, with example

# Control flow statements in Python are used to control the flow of execution of a program. They allow you to change the order in which statements are executed, and to repeat statements multiple times.

# There are three main types of control flow statements in Python:
# Conditional statements: allow you to execute different statements depending on whether a condition is true or false. The most common conditional statement is the if statement.
# Looping statements: allow you to repeat a block of statements multiple times. The most common looping statements are the for loop and the while loop.
# Jump statements: allow you to transfer control to a different part of the program. The most common jump statement is the break statement.

# Here is an example of a control flow statement in Python:
if age >= 18:
  print("You are old enough to vote.")
else:
  print("You are not old enough to vote.")
# This code checks whether the user is old enough to vote. If they are, it prints the message "You are old enough to vote." 
# Otherwise, it prints the message "You are not old enough to vote."

## IF Condition
x =-11
y=5
z=-9
if x > y :
    if z < 0:
        print ("x is greater than y")
    else:
        print ("x is less than y")

# IF-Else statement

x=5
if x > 0 :
    print("Positive")
elif x < 0 :
    print ("Negative")
else :
    print("Zero")


foods = ["Dahi Bhalay", "Chicken Karai", "Samosa Chart", "Daal Rice", "Biryani"]
for food in foods:
    print(food)

    # for(x=0, x>9, x++)
    # print(x)

    menu = ["Dahi Bhalay", "Chicken Karai", "Samosa Chart", "Daal Rice", "Biryani"]
for food in menu:
    print(food)  # it will print all items in menu variable one by one

    #the Above FOR Loop statement works, like we do manually as below;
    print(menu[0])  # for Dahi Bhalay
    print(menu[1])  # for Chicken Karai
    print(menu[2])  # for Samosa Chart
    print(menu[3])  # for Daal Rice  
    print(menu[4])  # for Biryani
    
# Another For loop Example
    ## FOR Loop with Break Controll statement
for letter in "Python":
    if letter == 'h':
        break       # this will break on letter h, and print only p, y, t letters.
    print(letter)
    print("Done!")
    print('End of program')

        ## FOR Loop with Continoue Controll statement. 
for letter in "Python":
    if letter == 'h':
        continue            # this will break (hide) on letter h, and print all others letters, like p, y, t, o, n.
    print(letter)
    print("Done!")
    print('End of program')

## FOR Loop with Pass Controll statement
for letter in "Python":
    if letter == 'h':
        pass             # this will pass the value on h, and print all letters
    print(letter)
    print("Done!")
    print('End of program')
    

    ## FOR Loop with Break statement
for letter in 'Python':
    count += 1
    print(count)
    break

## WHILE Loops
# Example No. 1
i = 1
while i < 6:
    print (i)
    i += 1
    print('Done!')

# Example No. 2
i = 0
while i < 3:
    j = 0
    while j < 3:
        print (i,j)
        j += 1
    i += 1
    print('Done!')

## For loop inside Whille loop
i =1
while i > 4:
    for j in range(3):  # range is function, and 3 is value
        print(i,j)
        i += 1

# while loop inside for loop for 
    for i in range(4): 
        j=1 
    while j < 5: 
        print(i, j) 
        j += 1



## SWITCH Case
    months = ['Jan', 'Feb', 'Mar']
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    switcher = {
            months[i]: day_of_week[i] for i in range(3)}
    month = input("Enter Month: ")
    weekday = switcher.get(month, "Invalid month")
    print(f"{month} falls on a {weekday}")
    case "Apr", "May":
    print("Spring Season")

    case "Jun", "Jul", "Aug":
    print("Summer Season")

    case "Sep", "Oct", "Nov":
    print("Autumn Season")
    
    case "Dec", "Jan":
    print("Winter Season")



#### Harry YT Python video  
## SWITCH CASE
    a = int(input("Enter yournNumber: "))
     
    match a:
    case 1:
    print("case is 1")
    case 2:
    Print("case is 2")
    case 13:
    Print("case is 13")
    case 42:
     Print("case is 13")
    case _:     # default case
    Print("Nothing Found in list")
    
    

## Nested Loops (For Inside For loop) - Nested means Loop within another loop, used for multi-dimentional data structure.


# Example No.1 
    colors = ['red', 'green', 'blue']
    items = ['pen', 'pencil', 'book']
    for color in colors:
        for item in items:
            print(color + "-" + item)  # this to get output as red-pen, green-pencil etc.
            print(color, item) # this to get output as red-pen, red-pencil, red-book, green-pen, green-pencil, and so on.
            # 9 times because there are 3 colors and 3 items


#Example no2
    for num in range(5):
        for char in "Python":
            print(char * num)

# For loop inside while loop
    colors = ['red', 'green', 'blue']
    count = 0
    while count <= len(colors):
        color = colors[count] # Get the current color from list of colors
        if color =='red':
            print ('Stop at red.')
            break # Exit the loop when we hit red
        else:
            print (color)
    else:
            print ("This is not a valid color.")


# For loop inside while loop

    for num in range(5):
        guess = int(input("Guess the number:"))
        if guess == randomNumber:
            print("You are correct!")
        else:
            print ("Sorry you guessed wrong.")


