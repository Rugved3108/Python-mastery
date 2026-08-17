#🐍 Python Day 8 — Dictionaries
## 🎯 Learning Objectives

By the end of Day 8, you should be able to:

Understand what a dictionary is
Create dictionaries
Work with key-value pairs
Access, add, update, and delete data
Check whether a key exists
Use .keys(), .values(), and .items()
Loop through dictionaries
Create nested dictionaries
Combine dictionaries with input(), loops, and built-in functions
Build a Student Information System

## 1. What is a Dictionary?

A dictionary is a Python data structure that stores data in key-value pairs.

Example
student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}

Here:

"name"    → "Rugved"
"age"     → 17
"branch"  → "Computer"
"name", "age", "branch" → keys
"Rugved", 17, "Computer" → values
Basic syntax
dictionary = {
    "key": value,
    "key": value
}

## 2. Why Use a Dictionary?

Suppose we use a list:

student = ["Rugved", 17, "Computer"]

To access the age:

print(student[1])

But we have to remember that index 1 means age.

With a dictionary:

student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}


print(student["age"])

This is easier to understand.

Remember
List       → access using index
Dictionary → access using key

## 3. Creating a Dictionary
student = {
    "name": "Rugved",
    "age": 17,
    "marks": 85
}


print(student)

Output:

{'name': 'Rugved', 'age': 17, 'marks': 85}

## 4. Accessing Values

Use the key inside square brackets:

student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}


print(student["name"])
print(student["age"])
print(student["branch"])

Output:

Rugved
17
Computer
Important
student["name"]

means:

Give me the value associated with the "name" key.

## 5. Adding a New Key-Value Pair

You can add new information:

student = {
    "name": "Rugved",
    "age": 17
}


student["branch"] = "Computer"


print(student)

Output:

{'name': 'Rugved', 'age': 17, 'branch': 'Computer'}
Pattern
dictionary["new_key"] = value

## 6. Updating a Value

If the key already exists, assigning a new value updates it.

student = {
    "name": "Rugved",
    "age": 17
}


student["age"] = 18


print(student)

Output:

{'name': 'Rugved', 'age': 18}
Remember
New key      → adds data
Existing key → updates data

## 7. Removing Data
del
student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}


del student["age"]


print(student)

Output:

{'name': 'Rugved', 'branch': 'Computer'}
pop()
student.pop("branch")

This removes the "branch" key.

## 8. Checking Whether a Key Exists

Use in.

student = {
    "name": "Rugved",
    "age": 17
}


print("name" in student)
print("marks" in student)

Output:

True
False
Example
if "age" in student:
    print("Age exists")

This is useful when working with user input.

## 9. Dictionary Methods

Python provides useful dictionary methods.

.keys()

Returns all keys.

student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}


print(student.keys())

Conceptually:

name
age
branch
.values()

Returns all values.

print(student.values())

Conceptually:

Rugved
17
Computer
.items()

Returns key-value pairs.

print(student.items())

Conceptually:

name → Rugved
age → 17
branch → Computer

## ⭐ Most important for loops
for key, value in student.items():
    print(key, value)

Output:

name Rugved
age 17
branch Computer

## 10. Looping Through a Dictionary
Loop through keys
student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}


for key in student:
    print(key)

Output:

name
age
branch
Loop through values
for value in student.values():
    print(value)

Output:

Rugved
17
Computer
Loop through keys and values
for key, value in student.items():
    print(key, ":", value)

Output:

name : Rugved
age : 17
branch : Computer
⭐ Remember this pattern
for key, value in dictionary.items():
    # code

You will use this frequently.

## 11. Meaningful Variable Names

Instead of:

for key, value in marks.items():
    print(key, value)

You can use:

for subject, score in marks.items():
    print(subject, score)

Both are correct.

The second version is often easier to understand because the variable names describe the data.

## 12. Dictionaries Can Store Different Data Types

A dictionary can contain different types of values.

student = {
    "name": "Rugved",
    "age": 17,
    "height": 5.8,
    "passed": True
}

Values can be:

String
Integer
Float
Boolean
List
Dictionary

## 13. Dictionary Containing a List
student = {
    "name": "Rugved",
    "marks": [85, 90, 78]
}

Access the list:

print(student["marks"])

Output:

[85, 90, 78]

Access an individual mark:

print(student["marks"][0])

Output:

85

Notice that we're combining:

Dictionary → key
List       → index

## 14. Nested Dictionaries

A dictionary can contain another dictionary.

student = {
    "name": "Rugved",
    "age": 17,
    "marks": {
        "Maths": 85,
        "Python": 95,
        "English": 90
    }
}

Structure:

student
│
├── name
├── age
│
└── marks
    ├── Maths
    ├── Python
    └── English

## 15. Accessing a Nested Dictionary

To access the marks:

print(student["marks"])

To access Python marks:

print(student["marks"]["Python"])

Output:

95
Understand the two steps
student["marks"]["Python"]

means:

student
   ↓
marks dictionary
   ↓
Python key
   ↓
95

## 16. Looping Through a Nested Dictionary
for subject, marks in student["marks"].items():
    print(subject, ":", marks)

Output:

Maths : 85
Python : 95
English : 90

This is one of the most important concepts from today's lesson.

## 17. Taking Dictionary Data from the User

We can combine dictionaries with input().

name = input("Enter student name: ").strip().title()
age = int(input("Enter student age: "))
branch = input("Enter branch: ")

Then create the dictionary:

student = {
    "name": name,
    "age": age,
    "branch": branch
}

The user provides the data instead of us hardcoding it.

## 18. Using sum() with Dictionary Values

Suppose:

marks = {
    "Maths": 85,
    "Python": 95,
    "English": 90
}

We can get the values:

marks.values()

Then calculate the total:

total = sum(marks.values())

So:

85 + 95 + 90 = 270

## 19. Using len() with a Dictionary
number_of_subjects = len(marks)

Since there are 3 subjects:

number_of_subjects = 3

This is useful for calculating an average.

average = total / number_of_subjects
Better than hardcoding:
average = total / 3

Because if you add another subject, the program automatically adjusts.

## 20. max() and min() with Dictionary Values
highest = max(marks.values())
lowest = min(marks.values())

Example:

Marks → 85, 95, 90


Highest → 95
Lowest  → 85

# 🚀 Day 8 Mini Project — Student Information System

We combined everything into one project.

name = input("Enter student name: ").strip().title()
age = int(input("Enter student age: "))
branch = input("Enter branch: ")


maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))


student = {
    "name": name,
    "age": age,
    "branch": branch,
    "marks": {
        "Maths": maths,
        "Python": python,
        "English": english
    }
}


print()
print("=" * 50)
print("STUDENT INFO SYSTEM".center(50))
print("=" * 50)


print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])


print("\nMarks:")


for subject, marks in student["marks"].items():
    print(subject, ":", marks)


total = sum(student["marks"].values())
number_of_subjects = len(student["marks"])
average = total / number_of_subjects


print("=" * 50)
print("Total:", total)
print("Average:", average)
print("Highest Marks:", max(student["marks"].values()))
print("Lowest Marks:", min(student["marks"].values()))
print("=" * 50)


if average >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")


print("=" * 50)

## 🧠 What You Learned Through the Project

This one project combines many concepts:

input()
   ↓
Type conversion
   ↓
Dictionary
   ↓
Nested dictionary
   ↓
.items()
   ↓
.values()
   ↓
for loop
   ↓
sum()
   ↓
len()
   ↓
max()
   ↓
min()
   ↓
if / else

This is exactly how programming knowledge starts becoming connected instead of being a collection of separate topics.

# 📝 Day 8 Exercises
## Exercise 1 — Basic Dictionary

Create a dictionary containing:

name
age
college
branch
city

Print each value separately.

## Exercise 2 — Update Dictionary

Create:

student = {
    "name": "Rugved",
    "age": 17,
    "marks": 80
}

Then:

Change the age
Change the marks
Add the branch
Print the final dictionary

## Exercise 3 — Key Search

Create:

student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}

Ask the user for a key:

Enter information you want:

Check whether that key exists.

## Exercise 4 — Subject Marks

Create a dictionary containing 5 subjects and their marks.

Use .items() to print:

Maths : 85
Science : 90
English : 78
Python : 95
Physics : 82

# 🔥 Day 8 Challenge

Create a Student Information System that:

Takes student information from the user
Stores it in a dictionary
Stores marks inside a nested dictionary
Displays the student information
Displays every subject and mark
Calculates total
Calculates average
Finds highest marks
Finds lowest marks
Displays Pass/Fail

## ⭐ Bonus

Try to make the program automatically handle any number of subjects rather than exactly 3.

## 📌 Quick Revision
Create
student = {
    "name": "Rugved",
    "age": 17
}
Access
student["name"]
Add
student["branch"] = "Computer"
Update
student["age"] = 18
Delete
del student["age"]
Check
"name" in student
Keys
student.keys()
Values
student.values()
Key + Value
student.items()
Loop
for key, value in student.items():
    print(key, value)
Nested dictionary
student["marks"]["Python"]
Dictionary values + built-in functions
sum(student["marks"].values())
max(student["marks"].values())
min(student["marks"].values())
len(student["marks"])

## 🎯 Day 8 Core Concept

Remember this:

Dictionary
    ↓
Key → Value
    ↓
.items() → key + value
.values() → values
.keys() → keys
    ↓
Nested dictionaries
    ↓
Loops + built-in functions
    ↓
Real-world data organization

# Day 8 = Dictionaries ✅

The goal isn't to memorize every method. The important skill is understanding how dictionaries organize real-world information and how to work with that information programmatically.