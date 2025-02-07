# 📌 **Week 1: Python Fundamentals**

## 🎯 **Objective**

By the end of this week, you should have a solid understanding of Python’s syntax, basic programming logic, and core fundamental concepts. You will also complete hands-on exercises and a mini-project to apply what you’ve learned.

---

## 📖 **Topics Covered**

### ✅ **1. Introduction to Python & Setting Up the Environment**

#### **What is Python?**

Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in web development, data science, automation, artificial intelligence, and more.

#### **Installing Python**

- Download Python from the official website: [python.org](https://www.python.org/)
- Install an Integrated Development Environment (IDE) such as:
  - **VS Code** (Recommended for general programming)
  - **PyCharm** (Best for professional development)
  - **Jupyter Notebook** (Best for data science and interactive coding)
- Verify installation:
  ```bash
  python --version
  ```
- Running a Python script:
  ```bash
  python filename.py
  ```

---

### ✅ **2. Variables, Data Types & Operators**

#### **Variables**

Variables store data in memory. Unlike other languages, Python does not require explicit variable declaration. Example:

```python
name = "John"
age = 25
height = 5.9
```

#### **Data Types**

Python has several built-in data types:

- **Integers (`int`)** – Whole numbers (e.g., `10`, `-5`)
- **Floats (`float`)** – Decimal numbers (e.g., `3.14`, `-0.5`)
- **Strings (`str`)** – Text data (e.g., `"Hello"`, `'Python'`)
- **Booleans (`bool`)** – `True` or `False`
- **Lists (`list`)** – Ordered collection (e.g., `[1, 2, 3]`)
- **Tuples (`tuple`)** – Immutable ordered collection (e.g., `(1, 2, 3)`)
- **Dictionaries (`dict`)** – Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

#### **Operators**

Operators perform operations on variables:

- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponentiation)
- **Comparison Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators:** `and`, `or`, `not`

Example:

```python
x = 10
y = 3
print(x + y)   # Addition: 13
print(x // y)  # Floor division: 3
print(x > y)   # Comparison: True
```

---

### ✅ **3. Taking User Input & Displaying Output**

Python allows users to input data using the `input()` function. The default data type for user input is a string, so conversion is necessary for numerical operations.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Converts input to integer
print("Hello, " + name + "! You are", age, "years old.")
```

---

### ✅ **4. Conditional Statements (if, elif, else)**

Conditional statements help control the flow of a program based on conditions.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")
```

- `if` executes when the condition is **True**
- `elif` (else if) checks additional conditions
- `else` executes if none of the conditions are met

Example with multiple conditions:

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

---

### ✅ **5. Loops (for, while, break, continue)**

Loops allow repetitive execution of code blocks.

#### **For Loop**

Used for iterating over a sequence (list, tuple, string, range, etc.).

```python
for i in range(5):
    print("Hello", i)
```

#### **While Loop**

Executes as long as the condition is `True`.

```python
num = 1
while num <= 5:
    print(num)
    num += 1
```

#### **Break & Continue**

- `break` exits the loop early
- `continue` skips the current iteration

```python
for i in range(10):
    if i == 5:
        break  # Stops the loop at 5
    print(i)
```

```python
for i in range(10):
    if i == 5:
        continue  # Skips 5
    print(i)
```

---

### ✅ **6. Introduction to Functions**

Functions allow code reusability and modularity.

#### **Defining and Calling Functions**

```python
def greet(name):
    print("Hello, " + name)

greet("Alice")
```

#### **Function with Return Value**

```python
def add(x, y):
    return x + y

result = add(5, 3)
print("Sum:", result)
```

---

### ✅ **7. Basic Debugging & Error Handling**

Python provides exception handling using `try-except` blocks to prevent runtime errors.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
```

---

## 🛠 **Hands-on Exercises**

### 🔹 **1. Check if a Number is Even or Odd**

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 🔹 **2. Simple Calculator using User Input**

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation")
```

### 🔹 **3. Multiplication Table of a Given Number**

```python
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

---

## 🎯 **Mini Project: Build a Simple Calculator**

```python
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %")

    num1 = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Error! Division by zero."
    elif operation == "%":
        result = num1 % num2
    else:
        result = "Invalid operation"

    print("Result:", result)

calculator()
```

---

### 🎯 **Summary of Week 1**

✅ Learned Python basics, syntax, and environment setup.  
✅ Understood variables, data types, and user input/output.  
✅ Practiced conditional statements and loops.  
✅ Explored functions and error handling.  
✅ Completed hands-on exercises and a mini-project.

---

🚀 **Next Step:** Get ready for **Week 2: Data Structures & File Handling!**

---

---

# **📌 Week 2: Lists, Functions & File Handling**

**Objective:** Learn how to store, manipulate, and process data efficiently in Python.

---

## **1️⃣ Lists, Tuples, and Dictionaries**

Python provides multiple ways to store and manipulate collections of data.

### **🔹 Lists (Ordered, Mutable)**

A **list** is an ordered collection that can hold multiple data types. Lists are **mutable**, meaning they can be changed after creation.

#### **✅ Creating a List**

```python
fruits = ["Apple", "Banana", "Cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14]
```

#### **✅ List Operations**

```python
fruits.append("Mango")  # Adds an item
fruits.insert(1, "Orange")  # Inserts at a specific index
fruits.remove("Banana")  # Removes an item
fruits.pop()  # Removes the last item
print(fruits[0])  # Accessing elements
print(len(fruits))  # Finding the length of the list
```

#### **✅ Looping Through a List**

```python
for fruit in fruits:
    print(fruit)
```

---

### **🔹 Tuples (Ordered, Immutable)**

A **tuple** is like a list but **cannot be modified** (immutable). Useful for fixed data like coordinates.

#### **✅ Creating a Tuple**

```python
coordinates = (10.5, 20.3)
print(coordinates[0])  # Accessing elements
```

Tuples are **faster** than lists and take up less memory.

---

### **🔹 Dictionaries (Key-Value Pairs, Mutable)**

A **dictionary** stores data as `key: value` pairs, allowing quick lookups.

#### **✅ Creating a Dictionary**

```python
student = {
    "name": "John",
    "age": 21,
    "major": "Computer Science"
}
```

#### **✅ Accessing and Modifying Dictionaries**

```python
print(student["name"])  # Get value by key
student["age"] = 22  # Updating a value
student["grade"] = "A"  # Adding a new key-value pair
del student["major"]  # Deleting a key
```

#### **✅ Looping Through a Dictionary**

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## **2️⃣ Functions – Defining and Using Functions**

Functions help **organize code** and **avoid repetition**.

#### **✅ Defining and Calling a Function**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

#### **✅ Returning Values**

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

#### **✅ Default Parameters**

```python
def power(num, exp=2):  # Default exponent is 2
    return num ** exp

print(power(3))  # 3² = 9
print(power(3, 3))  # 3³ = 27
```

#### **✅ Using Keyword Arguments**

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Bob")  # Order doesn't matter
```

---

## **3️⃣ File Handling – Reading and Writing to Files**

Python allows interaction with files using **read**, **write**, and **append** modes.

### **🔹 Writing to a File (`w` mode)**

Creates a file if it doesn’t exist or **overwrites** it.

```python
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.")
```

### **🔹 Reading from a File (`r` mode)**

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### **🔹 Appending to a File (`a` mode)**

Adds new content **without** deleting existing content.

```python
with open("example.txt", "a") as file:
    file.write("\nThis is a new line.")
```

### **🔹 Reading Line by Line**

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # `.strip()` removes extra spaces/newlines
```

---

## **4️⃣ Exception Handling – Preventing Errors**

Handling exceptions prevents program crashes.

### **🔹 Using `try-except`**

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)  # Might cause ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:  # Catch-all for unexpected errors
    print(f"An error occurred: {e}")
```

---

## **5️⃣ Introduction to String Manipulation**

Python provides powerful string functions.

### **🔹 Common String Methods**

```python
text = "  Hello, Python!  "
print(text.lower())  # Converts to lowercase
print(text.upper())  # Converts to uppercase
print(text.strip())  # Removes extra spaces
print(text.replace("Python", "World"))  # Replace words
print(text.split(","))  # Splitting into a list
```

---

## **6️⃣ Working with Python Modules**

Modules help extend Python’s functionality.

### **🔹 Using Built-in Modules**

```python
import math

print(math.sqrt(25))  # Square root of 25
print(math.pi)  # Value of pi
```

### **🔹 Using External Libraries**

Install using:

```
pip install requests
```

Example:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

---

# **🚀 Hands-on Exercises**

✅ **Find the Largest Number in a List**

```python
def find_max(numbers):
    return max(numbers)

print(find_max([10, 5, 8, 3]))  # Output: 10
```

✅ **Contact Manager Using a Dictionary**

```python
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name, "Contact not found")

add_contact("Alice", "12345")
print(search_contact("Alice"))
```

✅ **Read and Write to a File**

```python
with open("data.txt", "w") as file:
    file.write("Hello, File Handling!")

with open("data.txt", "r") as file:
    print(file.read())
```

---

# **🎯 Mini Project: Contact List Manager**

**Objective:** Build a program that allows users to **add, update, delete, and search** contacts, storing them in a file.

### **🔹 Full Code:**

```python
import json

filename = "contacts.json"

def load_contacts():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

def add_contact(name, phone):
    contacts[name] = phone
    save_contacts(contacts)

def search_contact(name):
    return contacts.get(name, "Contact not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        return "Contact deleted."
    return "Contact not found."

# Example Usage
add_contact("Alice", "12345")
print(search_contact("Alice"))
print(delete_contact("Alice"))
```

---

## **🔚 Summary**

- **Lists, Tuples, and Dictionaries** – Store and manipulate data.
- **Functions** – Write reusable code.
- **File Handling** – Read and write files.
- **Exception Handling** – Prevent crashes.
- **String Manipulation** – Work with text.
- **Modules** – Extend Python’s capabilities.

This structured approach ensures you grasp Python’s core concepts efficiently. 🚀

### **📚 Additional Resources**

- [Python Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python) for more in-depth learning. 📚

---

# **📌 Week 3: Object-Oriented Programming (OOP) in Python**

**Objective:** Learn how to use OOP concepts to write modular, reusable, and efficient code in Python.

---

## **1️⃣ Introduction to Object-Oriented Programming (OOP)**

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects rather than actions. It focuses on:

- **Encapsulation** (hiding data)
- **Abstraction** (simplifying complexity)
- **Inheritance** (reusing code)
- **Polymorphism** (using common methods across different classes)

---

## **2️⃣ Classes and Objects**

### **🔹 Defining a Class**

A **class** is a blueprint for creating objects.

```python
class Car:
    def __init__(self, brand, model, year):  # Constructor
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):  # Method
        print(f"{self.brand} {self.model} ({self.year})")

# Creating objects (instances)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Calling methods
car1.display_info()  # Output: Toyota Corolla (2020)
car2.display_info()  # Output: Honda Civic (2022)
```

### **🔹 `self` Keyword**

The `self` keyword refers to the instance of the class. It allows access to attributes and methods.

---

## **3️⃣ Encapsulation (Hiding Data)**

Encapsulation **restricts direct access** to variables to protect data.

### **🔹 Private Variables**

In Python, private variables are **indicated** with an underscore `_` or `__` (double underscore).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```

✅ You **cannot** access `__balance` directly (e.g., `account.__balance`).

---

## **4️⃣ Inheritance (Reusing Code)**

Inheritance allows a class to **inherit attributes and methods** from another class.

### **🔹 Creating a Parent Class**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")
```

### **🔹 Creating a Child Class**

```python
class Dog(Animal):
    def speak(self):  # Overriding method
        print(f"{self.name} barks.")

dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks.
```

✅ The `Dog` class **inherits** from `Animal` but **overrides** the `speak` method.

---

## **5️⃣ Polymorphism (Same Method, Different Behavior)**

Polymorphism allows different classes to **use the same method name but implement different behaviors**.

```python
class Bird:
    def move(self):
        print("Flies in the sky")

class Fish:
    def move(self):
        print("Swims in the water")

# Using polymorphism
for animal in [Bird(), Fish()]:
    animal.move()
```

✅ Both classes have a `move()` method but **different behaviors**.

---

## **6️⃣ Abstraction (Hiding Implementation)**

Abstraction allows **hiding details** and **exposing only essential features**.

### **🔹 Using Abstract Classes**

Abstract classes **cannot be instantiated** and must be subclassed.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Must be implemented in child classes

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

✅ The `Shape` class **enforces** that all subclasses must define `area()`.

---

## **7️⃣ `super()` Keyword (Calling Parent Methods)**

The `super()` function **calls methods from the parent class**.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def start(self):
        super().start()  # Call parent method
        print(f"{self.brand} {self.model} is now running.")

car = Car("Toyota", "Camry")
car.start()
```

✅ Output:

```
Starting the vehicle...
Toyota Camry is now running.
```

---

## **8️⃣ Class and Static Methods**

### **🔹 Class Methods (`@classmethod`)**

- Used when a method **modifies** the class state.

```python
class Company:
    employees = 0

    @classmethod
    def add_employee(cls):
        cls.employees += 1

Company.add_employee()
print(Company.employees)  # Output: 1
```

### **🔹 Static Methods (`@staticmethod`)**

- Used when a method **does not depend** on the class state.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))  # Output: 8
```

---

## **9️⃣ Magic Methods (`__init__`, `__str__`, `__len__`)**

Python provides special methods called **dunder (double underscore) methods**.

### **🔹 `__str__` (String Representation)**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 25)
print(person)  # Output: Alice, 25 years old
```

### **🔹 `__len__` (Custom Length Calculation)**

```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))  # Output: 3
```

---

# **🚀 Hands-on Exercises**

✅ **Create a Student Management System**

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average_grade(self):
        total = sum(student.get_grade() for student in self.students)
        return total / len(self.students)

# Usage
s1 = Student("Alice", 20, 85)
s2 = Student("Bob", 22, 90)
s3 = Student("Charlie", 21, 88)

course = Course("Python Programming")
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())  # Output: 87.67
```

---

# **🔚 Summary**

- **Encapsulation** – Restrict access to variables.
- **Inheritance** – Reuse code from parent classes.
- **Polymorphism** – Define common methods in multiple classes.
- **Abstraction** – Hide implementation details.
- **Magic Methods** – Customize object behavior.

Mastering OOP in Python helps build scalable, modular applications. 🚀

# **📌 Week 4: Advanced Python Concepts**

**Objective:** Learn advanced Python concepts such as error handling, file handling, regular expressions, decorators, generators, multithreading, and database interactions.

---

## **1️⃣ Exception Handling (Try, Except, Finally)**

Errors can cause programs to crash. Python handles errors using `try-except`.

### **🔹 Basic Exception Handling**

```python
try:
    x = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

✅ Output: `Cannot divide by zero!`

### **🔹 Handling Multiple Exceptions**

```python
try:
    num = int(input("Enter a number: "))  # ValueError possible
    print(10 / num)  # ZeroDivisionError possible
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### **🔹 Using `finally`**

The `finally` block always executes, even if an error occurs.

```python
try:
    f = open("data.txt", "r")
    content = f.read()
finally:
    f.close()  # Ensures file is closed
```

---

## **2️⃣ File Handling in Python**

Python allows reading/writing files using the `open()` function.

### **🔹 Opening a File**

```python
file = open("example.txt", "r")  # Open for reading
content = file.read()
print(content)
file.close()
```

### **🔹 Writing to a File**

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
```

✅ The `with` statement ensures the file is closed automatically.

### **🔹 Appending to a File**

```python
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")
```

### **🔹 Reading Files Line by Line**

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes extra spaces
```

---

## **3️⃣ Regular Expressions (Regex)**

Python's `re` module allows pattern matching.

### **🔹 Matching Patterns**

```python
import re

text = "My email is example@gmail.com"
match = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", text)
if match:
    print("Email found:", match.group())  # Output: example@gmail.com
```

### **🔹 Finding All Matches**

```python
text = "Phone numbers: 123-456-7890, 987-654-3210"
matches = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(matches)  # Output: ['123-456-7890', '987-654-3210']
```

### **🔹 Replacing Text**

```python
new_text = re.sub(r"apple", "orange", "I like apple pie")
print(new_text)  # Output: I like orange pie
```

---

## **4️⃣ Decorators (Modifying Functions)**

Decorators **modify functions** without changing their code.

### **🔹 Creating a Simple Decorator**

```python
def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def say_name():
    print("I'm Python.")

say_name()
```

✅ Output:

```
Hello!
I'm Python.
Goodbye!
```

### **🔹 Using Decorators with Arguments**

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
```

✅ Output:

```
Hello!
Hello!
Hello!
```

---

## **5️⃣ Generators (Efficient Iterators)**

Generators **generate values on the fly** without storing them in memory.

### **🔹 Creating a Generator**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

✅ Output:

```
5
4
3
2
1
```

### **🔹 Generator Expressions**

```python
squares = (x * x for x in range(5))
print(list(squares))  # Output: [0, 1, 4, 9, 16]
```

---

## **6️⃣ Multithreading (Parallel Execution)**

Python's `threading` module runs tasks **simultaneously**.

### **🔹 Creating Threads**

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Wait for thread to finish
```

✅ Threads **run in parallel**, improving efficiency.

---

## **7️⃣ Working with Databases (SQLite3)**

Python’s `sqlite3` module allows database interactions.

### **🔹 Connecting to a Database**

```python
import sqlite3

conn = sqlite3.connect("students.db")  # Creates or opens a database
cursor = conn.cursor()
```

### **🔹 Creating a Table**

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
conn.commit()
```

### **🔹 Inserting Data**

```python
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 22))
conn.commit()
```

### **🔹 Fetching Data**

```python
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

### **🔹 Closing the Connection**

```python
conn.close()
```

---

## **🔚 Summary**

| **Concept**         | **Key Takeaways**                                     |
| ------------------- | ----------------------------------------------------- |
| Exception Handling  | Use `try-except-finally` to handle errors gracefully. |
| File Handling       | Read, write, and append to files using `open()`.      |
| Regular Expressions | Use `re` module for pattern matching.                 |
| Decorators          | Modify functions dynamically.                         |
| Generators          | Generate values **efficiently** using `yield`.        |
| Multithreading      | Run tasks in **parallel** using `threading`.          |
| SQLite3             | Store and retrieve data using `sqlite3` database.     |

---

## **🚀 Hands-on Exercises**

✅ **1. Implement Exception Handling**
Write a program that asks for user input and handles both `ValueError` and `ZeroDivisionError`.

✅ **2. File Handling**
Write a Python script that reads a file, counts the number of words, and saves the count in a new file.

✅ **3. Regular Expressions**
Extract all email addresses from a given text file.

✅ **4. Create a Decorator**
Write a decorator that logs function execution time.

✅ **5. Use a Generator**
Write a generator that yields Fibonacci numbers.

✅ **6. Multithreading**
Create two threads: one prints even numbers, and the other prints odd numbers.

✅ **7. Database Handling**
Create an SQLite database and store user information.

---

By mastering these advanced Python concepts, you’ll be well-prepared to build **efficient, scalable, and powerful** applications! 🚀🔥

# **📌 Python Learning Summary (Week 2 - Week 4)**

| **Week**                                     | **Topics Covered**                                                                                                                                                                                                                                                                                                        | **Hands-on Exercises**                                                                                                                                                                                                                                                                | **Mini Project**                                                                                                                |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Week 2: Lists, Functions & File Handling** | ✅ Lists, Tuples, and Dictionaries (Adding, Removing, Updating Data) <br> ✅ Functions (Defining, Calling, Parameters) <br> ✅ File Handling (Reading/Writing Files) <br> ✅ Exception Handling (Try/Except Blocks) <br> ✅ String Manipulation <br> ✅ Importing Python Modules                                          | 🔹 Find the largest number in a list <br> 🔹 Store & retrieve contacts using a dictionary <br> 🔹 Read and write to a text file                                                                                                                                                       | 🎯 **Contact List Manager** – A program to add, update, delete, and search contacts stored in a file                            |
| **Week 3: Introduction to OOP & APIs**       | ✅ Object-Oriented Programming (OOP) <br> ✅ Defining Classes & Objects <br> ✅ Class Attributes, Methods & `__init__` Constructor <br> ✅ Working with APIs (Fetching Web Data) <br> ✅ Web Scraping (Extracting Information from Websites)                                                                              | 🔹 Create a `Car` class with attributes <br> 🔹 Fetch and display weather data using a public API <br> 🔹 Scrape product prices from an e-commerce website                                                                                                                            | 🎯 **Weather App using an API** – A Python script that fetches and displays real-time weather information based on user input   |
| **Week 4: Advanced Python Concepts**         | ✅ Exception Handling (Try/Except/Finally) <br> ✅ File Handling (Reading, Writing, Appending) <br> ✅ Regular Expressions (`re` module) <br> ✅ Decorators (Modifying Functions) <br> ✅ Generators (`yield` for efficient iteration) <br> ✅ Multithreading (Parallel Execution) <br> ✅ Database Handling with SQLite3 | 🔹 Implement exception handling for input validation <br> 🔹 Extract email addresses from a text file using regex <br> 🔹 Write a decorator to log function execution time <br> 🔹 Use a generator to yield Fibonacci numbers <br> 🔹 Create an SQLite database to store user details | 🎯 **Final Project (Choose One)**: <br> 🔹 To-Do List App <br> 🔹 Expense Tracker <br> 🔹 Simple Chatbot <br> 🔹 File Organizer |

This table provides a structured overview of your **Python learning path**, ensuring **gradual skill-building** from basic data structures to advanced programming concepts. 🚀🔥
