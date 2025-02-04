#  introduction to python

# what is python?
# is a high-level, interpreted programming language 
# that is widely used for various purposes such as web development, scientific computing, data analysis, ai

# why learn python?
# simple and easy to learn
# large community and resources
#  extensive libraries and frameworks e.g pandas
#  cross-platform compatibility


# ide or text editor?
#  -vs code
#  -pycharm
#  -sublime text

# 2 python syntax, variables and data types

# python syntax
#  -indentation is used to define block of code

#  -print() function is used to print output
# print("hello world") # prints hello world

# 2 .1 variables and data types

# example 

# name = "John" 
# Age = "30"
# df = "gideon"
# print(name,Age,df)

# data types
#  -strings
#  -integers
#  -floats
#  -boolean
#  -list
#  -tuple
#  -dictionary
#  -set
#  -complex

# strings - text e.g gideon, cow, goat,
#  -strings are immutable
#  -strings can be concatenated using the + operator
#  -strings can be sliced using the [ ] operator
#  -strings can be formatted using the % operator
#  -strings can be formatted using the f string operator
#  -strings can be formatted using the format() function
#  -strings can be formatted using the format_map() function

# example
# name = "gideon"
# print(name)

# intergers
#  -integers are whole numbers e.g 1, 2, 3,
#  -integers can be concatenated using the + operator
#  -integers can be sliced using the [ ] operator
#  -integers can be formatted using the % operator
#  -integers can be formatted using the f string operator
#  -integers can be formatted using the format() function
#  -integers can be formatted using the format_map() function
# example
# age = 30
# print(age)

# float - decimal 
#  -floats are decimal numbers e.g 1.2, 3.4,
#  -floats can be concatenated using the + operator
#  -floats can be sliced using the [ ] operator
#  -floats can be formatted using the % operator
#  -floats can be formatted using the f string operator

# example
# height = 1.8
# print(height)

# booleans
#  -booleans are true or false
#  -booleans can be concatenated using the + operator

# example
# is_adult = True
# print(is_adult)

# input/output, comments, control flow and functions
# input/output
#  -input() function is used to get user input
#  -print() function is used to print output to the screen
#  -input() function returns a string, so we need to convert it to the required data
#  -type() function is used to get the data type of a variable

# example
# name = input("Enter your name: ") # get user input
# print("Hello, " + name)

# comments
#  -comments are used to explain the code
#  -comments are ignored by the interpreter
#  -comments are used to make the code more readable
#  -comments are used to make the code more maintainable
#  -comments are used to make the code more understandable
#  -comments are used to make the code more debuggable

# example
# single-line comment
# this is a comment

# multi-line comment
# example
"""
this is a multi-line comment
it can span multiple lines
it can be used to explain complex code
it can be used to explain complex logic
"""

# control flow
# conditional statements
#  -if-else statement is used to execute different actions based on a condition

# example
# age = int(input("enter your age: "))
# if age >= 18:
#     print("you are an adult")
# else:
#     print("you are a minor")

# example of strings using if----else

# password = input("Enter your password: ")
# if len(password) > 5:
#     print("Your password is correct")
# else:
#     print("Your password is less than 8 characters")

#  if -elif-else statement is used to execute different actions based on multiple conditions
#  -elif is used to check the next condition if the previous condition is false

# example
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")
# elif age >= 13:
#     print("youre a teenager")
# elif age >= 9:
#     print("you are a pre-teen")
# else:
#     print("you are a kid")

# loops
#  -for loop is used to execute a block of code repeatedly for a specified number of times
# example
# for i in range(10):
#     print(i)
#  -while loop is used to execute a block of code repeatedly while a condition is true
# example
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# functions
#  -functions are used to group a block of code that can be called multiple times from different
#  parts of the program
#  defined using def

# example
# def greet(name):
#     return"Hello, " + name
# print(greet("Ivy!"))


