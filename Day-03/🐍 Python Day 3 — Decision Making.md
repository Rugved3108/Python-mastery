# 🐍 Python Day 3 — Decision Making

## 1. Conditions

A condition evaluates to either:

```python
True
False
```

Example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

---

# 2. `if`

`if` executes a block of code when a condition is `True`.

Syntax:

```python
if condition:
    # code
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

### Important

Python uses indentation to define the code inside the `if`.

Use **4 spaces**.

---

# 3. `if` + `else`

`else` executes when the `if` condition is `False`.

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Only one of the two blocks executes.

---

# 4. `elif`

`elif` allows multiple conditions.

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("F")
```

Python checks conditions from **top to bottom**.

Once a condition is `True`, the remaining `elif` blocks are skipped.

---

# 5. Order of Conditions Matters

❌ Bad:

```python
if marks >= 60:
    print("D")
elif marks >= 90:
    print("A")
```

For `95`, Python prints `D` because `95 >= 60` is already true.

✅ Better:

```python
if marks >= 90:
    print("A")
elif marks >= 60:
    print("D")
```

Put more specific/higher conditions first.

---

# 6. Comparison Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `==` | Equal |
| `!=` | Not equal |

Examples:

```python
age >= 18
marks == 100
number != 0
```

---

# 7. Logical Operators

## `and`

Both conditions must be `True`.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

```text
True and True → True
True and False → False
False and True → False
False and False → False
```

---

## `or`

At least one condition must be `True`.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

## `not`

Reverses a Boolean value.

```python
is_raining = False

if not is_raining:
    print("No umbrella needed")
```

```text
not True  → False
not False → True
```

---

# 8. Nested `if`

An `if` inside another `if`.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")
```

Use nested `if` when a second decision depends on the first decision.

---

# 9. Modulus in Conditions

`%` gives the remainder.

It is commonly used to determine whether a number is even or odd.

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Logic:

```text
number % 2 == 0 → Even
otherwise       → Odd
```

---

# 10. Input Cleaning

`.strip()` removes unnecessary spaces from the beginning and end of a string.

```python
operation = input("Enter operation: ").strip()
```

For example:

```text
"  +  "
```

becomes:

```text
"+"
```

---

# 11. Decision-Making Pattern

A useful way to think about programs:

```text
Input
  ↓
Condition
  ↓
Decision
  ↓
Result
```

Example:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# ⚠️ Common Mistakes

### Mistake 1 — Missing indentation

❌

```python
if age >= 18:
print("Adult")
```

✅

```python
if age >= 18:
    print("Adult")
```

---

### Mistake 2 — Using `=` instead of `==`

`=` means assignment:

```python
age = 18
```

`==` means comparison:

```python
age == 18
```

Remember:

```text
=   → assign
==  → compare
```

---

### Mistake 3 — Wrong condition order

Always consider which condition should be checked first.

---

### Mistake 4 — Forgetting edge cases

For example:

```python
number = 0
```

Zero is even because:

```python
0 % 2 == 0
```

---

# 🧠 Key Takeaways

```text
if       → first condition
elif     → another condition
else     → everything else

and      → both conditions
or       → at least one condition
not      → reverse Boolean

> < >= <= == != → comparisons

%        → remainder
.strip() → remove surrounding whitespace
```

---

# 🎯 Day 3 Skill

You can now write programs that:

**Take input → evaluate conditions → make decisions → produce different outputs.**

Examples you've built:

- Number analyzer
- Age checker
- Grade checker
- Even/odd checker
- Login system
- Smart calculator

These are your first real **decision-based programs**.