# 🐍 Python Day 11 — Modules & Imports

## 🎯 Day 11 Goals

By the end of Day 11, you should understand:

- What a module is
- Why modules are useful
- `import`
- `from ... import ...`
- `import ... as ...`
- Python's built-in modules
- Creating your own module
- Importing your own module
- `__name__ == "__main__"`
- Organizing Python programs into multiple files
- Combining modules with functions, loops, conditions, and exceptions

---

# 1. What is a Module?

A **module is a Python file (`.py`) containing reusable code.**

For example:

```text
calculator.py
```

can contain:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Another Python file can use these functions.

```text
main.py
```

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

Output:

```text
15
5
```

### Simple definition

> A module is a `.py` file that contains code we can reuse in another Python file.

---

# 2. Why Do We Need Modules?

Imagine putting a whole application into one file:

```text
main.py
```

It could contain:

- calculator functions
- student functions
- file functions
- validation functions
- game functions
- utility functions

As the program becomes larger, this becomes difficult to manage.

Instead, we can organize it:

```text
project/
│
├── main.py
├── calculator.py
├── students.py
├── file_manager.py
└── utilities.py
```

Each file has a specific responsibility.

### Main benefit

> Modules make large programs easier to organize, reuse, understand, and maintain.

---

# 3. `import`

The basic syntax is:

```python
import module_name
```

Example:

```python
import math
```

Now we can use functions from `math`:

```python
print(math.sqrt(25))
```

Output:

```text
5.0
```

The structure is:

```text
math
 ↓
sqrt()
 ↓
25
```

We write:

```python
math.sqrt(25)
```

because `sqrt()` belongs to the `math` module.

---

# 4. Important Built-in Modules

Python already provides many useful modules.

| Module | Purpose |
|---|---|
| `math` | Mathematical operations |
| `random` | Random numbers and choices |
| `datetime` | Date and time |
| `os` | Operating-system interaction |
| `pathlib` | File/folder paths |
| `json` | JSON data |
| `statistics` | Statistical calculations |

We will learn more of these later.

---

# 5. The `math` Module

```python
import math
```

### Square root

```python
print(math.sqrt(25))
```

Output:

```text
5.0
```

### Power

```python
print(math.pow(2, 3))
```

Output:

```text
8.0
```

### Ceiling

```python
print(math.ceil(4.2))
```

Output:

```text
5
```

### Floor

```python
print(math.floor(4.8))
```

Output:

```text
4
```

---

# 6. Exercise 1 — Math Module

Your solution:

```python
import math

number = float(input("Enter a number: "))

print("Square root:", math.sqrt(number))
print("Ceiling value:", math.ceil(number))
print("Floor value:", math.floor(number))
```

### Concepts used

- `import`
- `math`
- `float()`
- `input()`
- `sqrt()`
- `ceil()`
- `floor()`

### Result

✅ Correct

### Important note

`math.sqrt()` cannot calculate the square root of a negative number using this method.

---

# 7. `random` Module

The `random` module allows us to generate random values.

```python
import random
```

Generate a random integer:

```python
number = random.randint(1, 100)

print(number)
```

Every run can produce a different number.

For example:

```text
27
```

or:

```text
84
```

or:

```text
3
```

---

# 8. `random.randint()`

Syntax:

```python
random.randint(start, end)
```

Both values are included.

For example:

```python
random.randint(1, 6)
```

can generate:

```text
1
2
3
4
5
6
```

---

# 9. Exercise 2 — Random Number

Your solution:

```python
import random

number = random.randint(1, 100)

print("Random number between 1 and 100:", number)
```

✅ Correct.

---

# 10. Exercise 3 — Random Dice 🎲

Your solution:

```python
import random

number = random.randint(1, 6)

print(number)
```

✅ Correct.

A slightly more descriptive output could be:

```python
print("You rolled:", number)
```

---

# 11. `from ... import ...`

Instead of importing the entire module:

```python
import math
```

we can import a specific function:

```python
from math import sqrt
```

Now we can write:

```python
print(sqrt(25))
```

instead of:

```python
print(math.sqrt(25))
```

---

# 12. Import Multiple Functions

We can import multiple functions:

```python
from math import sqrt, ceil, floor
```

Then:

```python
print(sqrt(25))
print(ceil(4.2))
print(floor(4.8))
```

---

# 13. Import Using an Alias

An alias gives a module another name.

```python
import math as m
```

Now:

```python
print(m.sqrt(25))
```

Instead of:

```python
print(math.sqrt(25))
```

Another example:

```python
import random as r

print(r.randint(1, 100))
```

### Remember

```python
import module as short_name
```

---

# 14. Creating Your Own Module ⭐

This is one of the most important concepts of Day 11.

Create:

```text
Day11/
│
├── calculator.py
└── main.py
```

### calculator.py

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
```

Now `calculator.py` is our own module.

---

# 15. Importing Your Own Module

Inside `main.py`:

```python
import calculator
```

Now we can access its functions:

```python
calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)
```

Example:

```python
import calculator

result = calculator.add(10, 5)

print(result)
```

Output:

```text
15
```

---

# 16. How Python Finds Your Module

If you have:

```text
Day11/
│
├── main.py
└── calculator.py
```

and write:

```python
import calculator
```

Python looks for the module in locations available to its import system, including the current project directory.

That's why your files can work together.

---

# 17. `__name__` ⭐⭐⭐

This is one of the most confusing concepts at first.

Every Python file has a special variable:

```python
__name__
```

Python automatically sets its value.

Its value depends on how the file is being used.

---

# 18. Running a File Directly

Suppose:

```text
calculator.py
```

contains:

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculator is running directly.")
```

If we run:

```text
calculator.py
```

directly, Python sets:

```python
__name__ = "__main__"
```

Therefore:

```python
if __name__ == "__main__":
```

becomes:

```python
if True:
```

So the code runs.

---

# 19. Importing a File

Suppose:

```text
main.py
```

contains:

```python
import calculator
```

Now `calculator.py` is being imported.

Inside `calculator.py`:

```python
__name__
```

is approximately:

```text
calculator
```

not:

```text
__main__
```

Therefore:

```python
if __name__ == "__main__":
```

is false.

The code inside it doesn't automatically execute.

---

# 20. The Easy Meaning

Don't worry about memorizing the technical details.

Remember:

```python
if __name__ == "__main__":
```

means:

> **Run this code only when this file is being run directly.**

This is commonly used for testing a module or starting a program.

---

# 21. Example

### calculator.py

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

If you run `calculator.py` directly:

```text
30
```

But if `main.py` does:

```python
import calculator
```

the `print(add(10, 20))` doesn't automatically execute.

However, the `add()` function is still available.

---

# 22. Why Is This Useful?

Imagine your module contains:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))
```

The bottom section is useful for testing.

When the file is imported, those tests don't run automatically.

This keeps your module clean.

---

# 23. Your Own Module — Calculator

Your `calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

if __name__ == "__main__":
    print("Calculator module loaded successfully.")
```

Your `main.py`:

```python
import calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = calculator.add(num1, num2)
elif operation == "-":
    result = calculator.subtract(num1, num2)
elif operation == "*":
    result = calculator.multiply(num1, num2)
elif operation == "/":
    result = calculator.divide(num1, num2)
else:
    print("Invalid operation.")
    exit()

print("Result:", result)
```

### What this taught you

You combined:

```text
Functions
   +
Modules
   +
Input
   +
Conditions
   +
Exceptions
```

---

# 24. Day 11 Mini Project — Random Password Generator 🔐

## Project Goal

Create a password generator using separate Python files.

Project structure:

```text
Day11/
│
├── password_generator.py
└── main.py
```

---

# 25. `password_generator.py`

Your completed code:

```python
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

def generate_password(length):

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password
```

---

# 26. Understanding the Password Generator

### Characters

```python
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
```

This is the collection from which we randomly select characters.

It contains:

- lowercase letters
- uppercase letters
- numbers
- symbols

---

### Function

```python
def generate_password(length):
```

The function receives the desired password length.

For example:

```python
generate_password(8)
```

means:

> Generate a password containing 8 characters.

---

### Empty password

```python
password = ""
```

We start with nothing.

---

### Loop

```python
for _ in range(length):
```

If:

```python
length = 5
```

the loop runs 5 times.

---

### Random character

```python
random.choice(characters)
```

selects one random character.

For example:

```text
a
```

Then:

```text
7
```

Then:

```text
@
```

Then:

```text
K
```

Then:

```text
2
```

The password becomes:

```text
a7@K2
```

---

### Return

```python
return password
```

sends the generated password back to the caller.

---

# 27. `main.py`

Your completed code:

```python
import password_generator

def main():
    length = int(input("Enter the desired password length: "))
    password = password_generator.generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
```

This is a good structure.

---

# 28. Why Put `main()` in a Function?

Instead of writing everything directly:

```python
length = int(input(...))
password = ...
print(...)
```

we put the main program logic inside:

```python
def main():
```

Then:

```python
if __name__ == "__main__":
    main()
```

starts the program when `main.py` is run directly.

This makes the program easier to organize and reuse.

---

# 29. Your Day 11 Mistake — Duplicate Input

You initially wrote:

```python
def main():
    length = int(input("Enter the desired password length: "))
    password = password_generator.generate_password(length)
    print("Generated password: ", password)

    try:
        length = int(input("Enter the desired password length: "))
        ...
```

### Problem

You were asking for the length twice.

```text
Enter length: 10
Generated password: ...

Enter length: 12
Generated password: ...
```

You also had the first input **outside the `try` block**.

Therefore, if the user entered:

```text
abc
```

the program would crash before reaching `try`.

---

# 30. Correct Error-Handling Structure

Everything that can cause the `ValueError` should be inside `try`:

```python
def main():
    try:
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        password = password_generator.generate_password(length)

        print("Generated password:", password)

    except ValueError as e:
        print("Error:", e)
```

Now:

### User enters:

```text
abc
```

Result:

```text
Error: invalid literal for int() with base 10: 'abc'
```

### User enters:

```text
-5
```

Result:

```text
Error: Password length must be a positive integer.
```

### User enters:

```text
10
```

Result:

```text
Generated password: a7K@92mP$x
```

---

# 31. Another Important Mistake to Avoid

Don't unnecessarily duplicate code.

Bad:

```python
length = int(input(...))
password = generate_password(length)
print(password)

try:
    length = int(input(...))
    password = generate_password(length)
    print(password)
```

Better:

```python
try:
    length = int(input(...))

    if length <= 0:
        raise ValueError(...)

    password = generate_password(length)
    print(password)

except ValueError as e:
    print("Error:", e)
```

### General lesson

> Don't repeat the same operation when one clean block can handle it.

---

# 32. Common Day 11 Mistakes

## ❌ Mistake 1 — Forgetting `import`

Wrong:

```python
print(math.sqrt(25))
```

Correct:

```python
import math

print(math.sqrt(25))
```

---

## ❌ Mistake 2 — Wrong module function syntax

If you write:

```python
import calculator
```

you normally access the function as:

```python
calculator.add(5, 3)
```

not:

```python
add(5, 3)
```

unless you specifically imported `add`.

---

## ❌ Mistake 3 — Confusing `import` and `from`

```python
import math
```

requires:

```python
math.sqrt(25)
```

while:

```python
from math import sqrt
```

allows:

```python
sqrt(25)
```

---

## ❌ Mistake 4 — Putting testing code outside `__main__`

If you have:

```python
print("Testing...")
```

outside:

```python
if __name__ == "__main__":
```

that code will execute when the module is imported.

---

## ❌ Mistake 5 — Not understanding `__name__`

Remember:

### Direct execution

```text
file.py
 ↓
__name__ = "__main__"
```

### Import

```text
import file
 ↓
__name__ = "file"
```

Therefore:

```python
if __name__ == "__main__":
```

runs only during direct execution.

---

## ❌ Mistake 6 — Division by zero

Your calculator correctly handled this:

```python
if b == 0:
    raise ValueError("Denominator cannot be zero.")
```

This prevents:

```python
10 / 0
```

from silently producing an incorrect result.

---

## ❌ Mistake 7 — Putting `try` too late

If this is outside:

```python
try:
    ...
```

then errors from it aren't caught.

For example:

```python
length = int(input(...))

try:
    ...
```

doesn't protect the `int()` conversion.

Instead:

```python
try:
    length = int(input(...))
```

---

# 33. Important Concepts You Learned Today

### Module

```text
A reusable Python file.
```

### Import

```python
import calculator
```

### Specific import

```python
from math import sqrt
```

### Alias

```python
import random as r
```

### Own module

```text
calculator.py
```

### Module function

```python
calculator.add(5, 3)
```

### Main check

```python
if __name__ == "__main__":
```

### Random choice

```python
random.choice(characters)
```

### Random integer

```python
random.randint(1, 100)
```

---

# 📝 Day 11 Cheat Sheet

```python
# Import entire module
import math

# Use module function
math.sqrt(25)


# Import specific function
from math import sqrt

sqrt(25)


# Import multiple functions
from math import sqrt, ceil, floor


# Alias
import random as r

r.randint(1, 10)


# Own module
import calculator

calculator.add(5, 3)


# Main check
if __name__ == "__main__":
    main()


# Random integer
random.randint(1, 6)


# Random choice
random.choice("abcdef")
```

---

# 🧠 Day 11 Mental Model

Think about a Python project like a toolbox.

```text
                    PROJECT
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   calculator.py   users.py      file_manager.py
        │              │              │
     functions      functions      functions
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                    main.py
                       │
                    imports
                       ↓
                  uses functions
```

Modules allow us to break a large program into smaller, manageable pieces.

---

# 🎯 Day 11 Practice

Before moving to Day 12, you should be comfortable with these:

### Basic

1. Use `math`
2. Use `random`
3. Use `random.randint()`
4. Use `random.choice()`
5. Use `from ... import ...`
6. Use aliases

### Intermediate

7. Create your own module
8. Import your module
9. Call functions from your module
10. Understand `__name__ == "__main__"`

### Project level

11. Separate code into multiple files
12. Combine modules + functions + loops + conditions
13. Handle errors using `try/except`

---

# 🏆 Day 11 Final Result

You progressed from:

```text
One Python file
```

to:

```text
Multiple Python files
        ↓
Modules
        ↓
Imports
        ↓
Reusable functions
        ↓
Better project organization
```

Your **Random Password Generator** was your first proper multi-file project.

### Day 11 status: ✅ COMPLETED

**Next: Day 12 — Scope, `*args`, and `**kwargs`**

Day 12 will make your understanding of Python functions much stronger and introduce some powerful techniques used in real Python programs.