# 🐍 Python Day 1 — Basics

## 1. Python Program

A program is a set of instructions that a computer executes.

Python generally executes code from **top to bottom**.

```python
print("Hello")
print("My name is Rugved")
print("I am learning Python")
```

Output:

```text
Hello
My name is Rugved
I am learning Python
```

---

## 2. Variables

A variable is a name used to store a value.

```python
name = "Rugved"
age = 18
marks = 95
```

Here:

- `name` → stores text
- `age` → stores an integer
- `marks` → stores an integer

Print variables:

```python
print(name)
print(age)
print(marks)
```

### Naming Rules

✅ Valid:

```python
age = 18
student_name = "Rugved"
marks1 = 90
```

❌ Invalid:

```python
1age = 18
student name = "Rugved"
```

### Python Naming Convention

Use **snake_case** for variable names:

```python
birth_year = 2008
current_year = 2026
favorite_food = "Pizza"
student_name = "Rugved"
```

Prefer lowercase variable names.

---

## 3. `print()`

`print()` displays information on the screen.

```python
print("Hello")
```

Print a variable:

```python
name = "Rugved"
print(name)
```

Print multiple values:

```python
name = "Rugved"
age = 18

print(name, age)
```

---

## 4. `input()`

`input()` gets information from the user.

```python
name = input("Enter your name: ")

print("Hello", name)
```

### Important

`input()` always returns a **string (`str`)**.

For example:

```python
age = input("Enter your age: ")
```

Even if the user enters:

```text
18
```

Python initially stores it as:

```python
"18"
```

---

## 5. Converting Input

Use `int()` when you need a whole number:

```python
age = int(input("Enter your age: "))
```

Use `float()` for decimal numbers:

```python
height = float(input("Enter your height: "))
```

---

## 6. Basic Calculations

```python
num1 = 10
num2 = 20

print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division
```

---

## 7. f-Strings

f-strings allow variables to be inserted directly into text.

```python
name = "Rugved"
age = 18

print(f"Hello {name}!")
print(f"You are {age} years old.")
```

This is usually cleaner than:

```python
print("Hello", name)
```

---

## 8. Useful String Methods

### `.title()`

Makes the first letter of words uppercase.

```python
name = input("Enter your name: ").title()
```

Input:

```text
rugved
```

Result:

```text
Rugved
```

### `.upper()`

Converts text to uppercase.

```python
name = "Rugved"

print(name.upper())
```

Output:

```text
RUGVED
```

---

## 9. `print()` and New Lines

Empty `print()` creates a blank line:

```python
print()
```

`\n` represents a new line:

```python
print("\nHello")
```

You can repeat strings using `*`:

```python
print("*" * 20)
```

Output:

```text
********************
```

---

# 🧪 Day 1 Example Program

```python
name = input("Enter your name: ").title()
favorite_programming_language = input(
    "Enter your favorite programming language: "
).title()

current_year = 2026
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print("\n" + "*" * 20)
print(f"WELCOME {name.upper()}")
print("*" * 20)

print(f"\nHello {name}!")
print(f"You are {age} years old.")
print(
    f"Your favorite programming language is "
    f"{favorite_programming_language}."
)

print("\nHave a great day ahead!")
```

---

# ⚠️ Common Beginner Mistakes

### Mistake 1 — Forgetting quotes

❌

```python
print(Hello)
```

✅

```python
print("Hello")
```

---

### Mistake 2 — Doing calculations with string input

❌

```python
age = input("Enter age: ")
print(age + 1)
```

✅

```python
age = int(input("Enter age: "))
print(age + 1)
```

---

### Mistake 3 — Incorrect variable names

❌

```python
student name = "Rugved"
```

✅

```python
student_name = "Rugved"
```

---

# 🧠 Day 1 Key Takeaways

Remember these:

```text
print()       → display output
input()       → get user input
int()         → convert to integer
float()       → convert to decimal number
str()         → convert to string
variable      → stores a value
f"..."        → formatted string
.title()      → capitalize words
.upper()      → uppercase text
\n            → new line
```

## 🎯 Day 1 Skill

You should now be able to create a basic interactive Python program using:

**Variables → Input → Processing → Output**

That is the fundamental pattern behind many programs.