# 🐍 Python Day 2 — Data Types, Type Conversion & Operators

## 1. Data Types

A **data type** tells Python what kind of value a variable stores.

### Main Python Data Types

| Type | Example | Meaning |
|---|---|---|
| `int` | `18` | Whole number |
| `float` | `3.14` | Decimal number |
| `str` | `"Hello"` | Text |
| `bool` | `True` / `False` | Boolean value |

Example:

```python
age = 18
height = 5.8
name = "Rugved"
is_student = True
```

---

## 2. Checking Data Type

Use `type()`:

```python
age = 18
print(type(age))
```

Output:

```text
<class 'int'>
```

Example:

```python
name = "Rugved"
age = 18
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

---

# 3. Integer — `int`

An integer is a whole number.

```python
age = 18
marks = 95
temperature = -5
```

Examples:

```text
10
0
-25
1000
```

---

# 4. Float — `float`

A float is a number containing a decimal value.

```python
height = 5.8
pi = 3.14159
temperature = 36.5
```

---

# 5. String — `str`

A string represents text.

```python
name = "Rugved"
city = "Mumbai"
language = "Python"
```

Anything inside quotes is treated as a string.

```python
100      # int
"100"    # str
```

These are different data types.

---

# 6. Boolean — `bool`

A Boolean has only two possible values:

```python
True
False
```

Example:

```python
is_student = True
is_raining = False
```

Boolean values are especially important for conditions and decision-making.

---

# 7. Type Conversion

Type conversion means changing a value from one data type to another.

### String → Integer

```python
age = "18"

age = int(age)

print(age)
print(type(age))
```

### String → Float

```python
height = "5.8"

height = float(height)
```

### Integer → Float

```python
marks = 95

marks = float(marks)

print(marks)
```

Output:

```text
95.0
```

### Integer → String

```python
age = 18

age = str(age)

print(type(age))
```

---

# 8. Important `input()` Rule

`input()` always returns a string.

```python
age = input("Enter your age: ")
```

Even if the user enters:

```text
18
```

Python receives:

```python
"18"
```

Therefore, when numerical input is required:

```python
age = int(input("Enter your age: "))
```

For decimal input:

```python
height = float(input("Enter your height: "))
```

---

# 9. Arithmetic Operators

Arithmetic operators are used for calculations.

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Power | `10 ** 3` | `1000` |

### Examples

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 10. Floor Division — `//`

Returns the floor of the division result.

```python
print(15 // 4)
```

Output:

```text
3
```

Because:

```text
15 / 4 = 3.75
```

`//` gives `3`.

---

# 11. Modulus — `%`

Returns the remainder after division.

```python
print(15 % 4)
```

Output:

```text
3
```

Because:

```text
15 = 4 × 3 + 3
```

Modulus is very useful for problems involving:

- Even/odd numbers
- Remainders
- Cycles
- Divisibility

Example:

```python
number = 10

print(number % 2)
```

Output:

```text
0
```

---

# 12. Power — `**`

Used for exponentiation.

```python
print(2 ** 5)
```

Output:

```text
32
```

Equivalent to:

```text
2 × 2 × 2 × 2 × 2
```

---

# 13. Comparison Operators

Comparison operators compare values.

They always produce a Boolean:

```text
True
False
```

| Operator | Meaning | Example |
|---|---|---|
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal | `10 >= 10` |
| `<=` | Less than or equal | `5 <= 10` |
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |

Examples:

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
print(10 >= 10)
print(5 <= 10)
```

---

# 14. Assignment Operators

Basic assignment:

```python
x = 10
```

Shortcut operators:

```python
x += 5
x -= 2
x *= 3
x /= 4
```

For example:

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

This is equivalent to:

```python
x = x + 5
```

---

# 15. String + String

The `+` operator can join strings.

```python
first_name = "Rugved"
last_name = "Patil"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Rugved Patil
```

This process is called **concatenation**.

---

# 16. String Multiplication

A string can be multiplied by an integer.

```python
print("Hi" * 3)
```

Output:

```text
HiHiHi
```

It repeats the string.

---

# ⚠️ Common Mistakes

## Mistake 1 — Adding string and integer

❌

```python
age = "18"

print(age + 2)
```

This causes a `TypeError`.

✅

```python
age = int(age)

print(age + 2)
```

---

## Mistake 2 — Confusing `=` and `==`

```python
x = 10
```

`=` means **assignment**.

```python
x == 10
```

`==` means **comparison**.

Remember:

```text
=   → assign
==  → compare
```

---

## Mistake 3 — Forgetting that input is a string

❌

```python
num1 = input("Enter number: ")
num2 = input("Enter number: ")

print(num1 + num2)
```

If the user enters:

```text
10
20
```

Output:

```text
1020
```

Because Python is joining strings.

✅

```python
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

print(num1 + num2)
```

Output:

```text
30
```

---

# 🧠 Programmer Thinking

Before writing code, identify:

### 1. Input

What information does the program receive?

### 2. Processing

What calculations or logic are required?

### 3. Output

What should the program display?

Example:

```text
Student Marks Calculator

Input
↓
3 subject marks

Processing
↓
Calculate total
↓
Calculate average

Output
↓
Total
Average
```

This **Input → Processing → Output** pattern is fundamental to programming.

---

# 📝 Day 2 Key Takeaways

Remember these:

```text
int       → whole numbers
float     → decimal numbers
str       → text
bool      → True / False

type()    → check data type

int()     → convert to integer
float()   → convert to float
str()     → convert to string

+         → addition
-         → subtraction
*         → multiplication
/         → division
//        → floor division
%         → remainder
**        → power

>         → greater than
<         → less than
>=        → greater/equal
<=        → less/equal
==        → equal
!=        → not equal

=         → assignment
+=        → add and assign
-=        → subtract and assign
*=        → multiply and assign
/=        → divide and assign

input()   → always returns str
```

---

# 🎯 Day 2 Skill

You should now understand:

**Data → Type → Conversion → Operation → Result**

Example:

```python
age = int(input("Enter age: "))

print(age + 1)
```

The process is:

```text
User input
    ↓
String
    ↓
int()
    ↓
Integer
    ↓
+ 1
    ↓
Result
```

---

# 🔥 Practice From Day 2

Problems you completed:

- Data type identification
- Type conversion
- Arithmetic calculations
- Comparison operations
- Student result calculator

Keep your original practice code separately from these notes. Your **notes explain the concept; your practice folder contains your actual coding attempts.**

Next topic: **Day 3 — `if`, `elif`, `else` and decision making.**