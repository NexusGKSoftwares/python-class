# variables
# 1. variables are used to store data
# 2. variables are used to perform operations

# example

# name = "John"  # variable name is assigned the value "John"
# age = 25  # variable age is assigned the value 25
# print(name)  # prints "John"
# print(age)

# data types
# string - alphabets and special characters
# integer - whole numbers
# float - decimal numbers
# boolean - true or false

# string
# name = "John"
# print(name)  # prints "John"

# integer
# age = 25
# print(age)  # prints 25

# float
# height = 1.75
# print(height)  # prints 1.75

# boolean
# is_adult = True
# print(is_adult)  # prints True

# input/output, comments,control flow, functions

# input
# name = input("Enter your name: ")
# print("Hello, " + name)  # prints "Hello, John" -- output

# example
# password
"""
password = input("Enter your password: ")
print("Your password is: " + password)  # prints "Your password is: " --output
"""
# comments
# comments are used to explain the code
# comments are ignored by the interpreter
# comments are used to make the code understandable
# comments are used to make the code maintainable
# example
# name = "John"  # this is a comment
# -- single line
"""
this is a
multi-line comment

""" #-- multi line

# control flow
# conditional statements
# if-else statements
# example
# age = 25
# if age >= 18:
#     print("You are an adult")  # prints "You are an adult"
# else:
#     print("You are not an adult")  # prints nothing

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")  # prints "You are an adult"
# else:
#     print("youre not an adult")  # prints nothing

# if ---- elif ---- else

# example
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")  # prints "You are an adult"
# elif age >= 13:
#     print("youre a teenager")  # prints "youre a teenager"
# else:
#     print("Youre a kid")  # prints "Youre a kid"
    
# example of a password
# password = input("Enter your password: ")
# if len(password) > 8:
#     print("your password is correct")
# elif len(password) == 8:
#     print("your password is almost correct")    
# else:
#     print("Please re-enter your password")
    

# Loops
# for loop
# what is for loop?

# example
# for i in range(5): # 0+1, 1+1, 2+1, 3+1, 4+1
#     print(i)  # prints 0, 1, 2, 3,

# another example
# for i in range(10): # 0+1, 1+1, 2+1, 3+1, 4+1, 5+1, 6+1, 7+1, 8+1,9+1
#     print(i)  # prints 0, 1, 2, 3,

# while ---- loop

# example
# i = 0
# while i < 5: # 0 < 5, 1 < 5,
#     print(i)  # prints 0, 1, 2, 3,
#     i += 1  # i = 0+1, i = 1+1
    
# example 2

# count = 0
# while count < 10:
#     print(count)  # prints 0, 1, 2, 3,
#     count += 1  # count = 0+1, count = 1+1

# functions

# what is a function?
# a function is a block of code that can be called multiple times from your program.
# it can take arguments and return values.
# example of a function
#  defined as "def"

def greet(name):
    return "Hello, " + name
print(greet("Ivy"))


