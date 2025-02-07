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


