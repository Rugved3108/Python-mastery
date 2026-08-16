# 🐍 Python Day 4 — Loops

## 1. What is a Loop?

A loop repeats a block of code automatically.

Without a loop:

```python
print("Hello")
print("Hello")
print("Hello")
```

With a loop:

```python
for i in range(3):
    print("Hello")
```

---

# 2. `for` Loop

Used to iterate through a sequence or repeat something a known number of times.

Syntax:

```python
for variable in sequence:
    # code
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

# 3. `range()`

`range()` generates a sequence of numbers.

### `range(stop)`

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

### `range(start, stop)`

```python
range(2, 6)
```

Produces:

```text
2 3 4 5
```

### `range(start, stop, step)`

```python
range(2, 11, 2)
```

Produces:

```text
2 4 6 8 10
```

### Important Rule

> **Start is included, stop is excluded.**

---

# 4. Counting Backwards

Use a negative step.

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

---

# 5. Loop Through a String

```python
name = "Rugved"

for letter in name:
    print(letter)
```

Output:

```text
R
u
g
v
e
d
```

Each character is processed one at a time.

---

# 6. `while` Loop

A `while` loop continues while a condition is `True`.

Syntax:

```python
while condition:
    # code
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# 7. Avoiding Infinite Loops

Be careful with:

```python
count = 1

while count <= 5:
    print(count)
```

`count` never changes, so the condition always remains `True`.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# 8. `for` vs `while`

### Use `for`

When iterating over a sequence or when the number of iterations is known.

```python
for i in range(10):
    print(i)
```

### Use `while`

When repetition depends on a condition and the number of repetitions isn't known.

```python
while password != "python":
    password = input("Enter password: ")
```

---

# 9. `break`

`break` immediately stops the loop.

```python
for i in range(1, 11):

    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

Think:

```text
break → STOP LOOP
```

---

# 10. `continue`

`continue` skips the current iteration and moves to the next iteration.

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

Think:

```text
continue → SKIP THIS ITERATION
```

---

# 11. Accumulator Pattern

An accumulator stores a result that changes during a loop.

Example:

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output:

```text
15
```

The pattern is:

```text
Initialize
    ↓
Loop
    ↓
Update
    ↓
Final result
```

This pattern is extremely common in programming.

---

# 12. Nested Loops

A loop inside another loop.

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)
```

The inner loop runs completely for each iteration of the outer loop.

---

# 13. Combining Loops and Conditions

Loops and `if` statements are frequently used together.

Example:

```python
for i in range(1, 11):

    if i % 2 == 0:
        print(i)
```

This means:

```text
Loop through numbers 1–10
        ↓
Check each number
        ↓
Is it even?
        ↓
Yes → print
No  → skip
```

---

# 14. Number Guessing Game Pattern

A `while True` loop can continue until `break`.

```python
secret_number = 7

while True:

    guess = int(input("Guess: "))

    if guess == secret_number:
        print("Correct!")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")
```

Important pattern:

```text
while True
    ↓
repeat
    ↓
check condition
    ↓
success?
    ↓
break
```

---

# ⚠️ Common Mistakes

### Mistake 1 — Forgetting that `range()` excludes stop

```python
range(1, 5)
```

produces:

```text
1 2 3 4
```

not 5.

---

### Mistake 2 — Infinite `while` loop

Always make sure something can eventually make the condition `False`, or use an appropriate `break`.

---

### Mistake 3 — Confusing `break` and `continue`

```text
break
→ stop the entire loop

continue
→ skip only the current iteration
```

---

# 🧠 Day 4 Key Takeaways

```text
for       → iterate/repeat
while     → repeat while condition is True
range()   → generate number sequences
break     → stop loop
continue  → skip current iteration
```

Important patterns:

```python
for i in range(...):
    ...
```

```python
while condition:
    ...
```

```python
total = 0

for i in ...:
    total += i
```

---

# 🎯 Day 4 Skill

You can now build programs that:

**Repeat → Check → Process → Update → Repeat**

You built:

- Number counter
- Even-number generator
- Multiplication-table generator
- Sum calculator
- Countdown
- Number Guessing Game

This is your first major step toward writing programs that actually **automate work**.