# Indentation 

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



# User Input program

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