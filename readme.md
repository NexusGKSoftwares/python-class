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