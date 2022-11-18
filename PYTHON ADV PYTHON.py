print("Hello Friend")
print("Hello 'Friend' world")
print('Hello "Friend" World')

## Escape sequence

print("Hello \"Friend\" Friend")

print("line A")
print("line B")

print("line A\nline B")                                 # above line can also be written like this  \n is for new line

print("line A\tline B")                                 # above line can also be written like this  \n is for new tab

print("this is double backslash \\\\")                  #output:\\

print("these are mountains /\\/\\/\\/\\")               #output:/\/\/\/\

print("he is \t awesome")                               #output:he is    awesome

print("\\\"\\n\\t\\\'")                                 ##output:\"n\t\'

print(r"line A\nline B")                                 # by using r we can treat escape sequence like normal string

print(2+3)

print(2+3*4)

# variables

num1 = 2
print(num1)


# string,number,  ctrl+/ to comment out multiple lines

_name = "vishal"
print(_name)



# string concatenation

first_name = "John"
last_name = "Mahire"
full_name =  first_name+" "+last_name
print(full_name)

# can not add or concatenate int and str  ("John"+3)<<-------- not possible
# but can do following

print("john"+"3")

print("john"+str(3))


print("john"*3)     # this will multiply and will give john 3 times


# # user input
# input function

name = input("Enter your name")
print("hello"+ name)                    # it will print hello and name entered
# the input always will be str even if it is number but still it will be taken as a str

# how to add (sum) two numbers
num1 = input("enter num1:")
num2 = input("enter num2:")
total = num1+num2
print("totalis" + total)

# above code will not make sum
# because
# it takes as str
# so we must define int fun there
# then the program will be

num1 =int( input("enter num1 :"))
num2 = int(input("enter num2 :"))
total = num1 + num2
print("total is : "+str(total))

# same can be used for float

# string formatting
 name = "John"
 age = "24"

 print("Hello {} Your age is {}".format(name,age))

 print(f"Hello {name} Your age is {age}")               # Using f string ----------> string formatting


#calculate avg of three numbers
num1 = input ("enter num1:")
num2 =input ("enter num2:")
num3 =input ("enter num3:")

#(int(num1)+int(num2)+int(num3))/3

print(f"The avg of these numbers is:{(int(num1)+int(num2)+int(num3))/3}")


# how to write input in one line
num1,num2,num3 = input("Enter three numbers comma seperated").split(",")

print(f"The avg of these numbers is:{(int(num1)+int(num2)+int(num3))/3}")


#Sting Indexing

lang = "python"         # lang is variable and "python is str"

# positions (index numbers)

# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2    
# n = 5, -1  

# print(lang[])               #always remember============ in python we use square bracket for indexing=========

print(lang[2])

print(lang[-1])






























































































































