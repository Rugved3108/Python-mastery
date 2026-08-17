# 🐍 Python Day 6 — Lists

1. What is a List?

A list is a collection of multiple values stored in one variable.

favorite_foods = ["paneer", "pavbhaji", "shrikhand", "biryani"]

A list can contain multiple values:

numbers = [10, 20, 30, 40, 50]
names = ["Rugved", "Aman", "Rahul"]

Lists can contain different data types:

data = ["Rugved", 18, 5.8, True]
2. List Indexing

Lists use indexes just like strings.

fruits = ["apple", "banana", "mango"]

Index positions:

apple    banana    mango
  0         1        2

Example:

print(fruits[0])
print(fruits[1])
print(fruits[2])

Output:

apple
banana
mango
Negative Indexing
print(fruits[-1])

Output:

mango

Useful:

fruits[0]     # First item
fruits[-1]    # Last item
3. len() with Lists

len() tells us how many items are inside a list.

fruits = ["apple", "banana", "mango"]


print(len(fruits))

Output:

3

Example:

students = ["Rugved", "Aman", "Rahul", "Priya"]


print("Total students:", len(students))
4. Changing a List Item

Lists are mutable, which means their values can be changed.

fruits = ["apple", "banana", "mango"]


fruits[1] = "orange"


print(fruits)

Output:

['apple', 'orange', 'mango']

We changed:

fruits[1]

from "banana" to "orange".

5. .append()

.append() adds an item to the end of a list.

fruits = ["apple", "banana", "mango"]


fruits.append("orange")


print(fruits)

Output:

['apple', 'banana', 'mango', 'orange']

Think:

append → add at the end
6. .insert()

.insert() adds an item at a specific position.

Syntax:

list.insert(index, value)

Example:

fruits = ["apple", "banana", "mango"]


fruits.insert(1, "grapes")


print(fruits)

Output:

['apple', 'grapes', 'banana', 'mango']

"grapes" was inserted at index 1.

7. .remove()

.remove() removes a specific value from a list.

fruits = ["apple", "banana", "mango"]


fruits.remove("banana")


print(fruits)

Output:

['apple', 'mango']

Important:

fruits.remove("banana")

removes the value, not the index.

8. del

del can remove an item using its index.

fruits = ["apple", "banana", "mango"]


del fruits[1]


print(fruits)

Output:

['apple', 'mango']

Difference:

fruits.remove("banana")   # Remove by value
del fruits[1]             # Remove by index
9. Loop Through a List

A for loop can process every item in a list.

fruits = ["apple", "banana", "mango"]


for fruit in fruits:
    print(fruit)

Output:

apple
banana
mango

This is very important because loops + lists are used constantly in programming.

10. Check if an Item Exists

Use the in operator.

students = ["Rugved", "Aman", "Rahul", "Priya"]


if "Rugved" in students:
    print("Student found!")

Output:

Student found!

User input example:

student_name = input("Enter student name: ").strip().title()


if student_name in students:
    print("Student found!")
else:
    print("Student not found.")
11. sum()

sum() calculates the total of numbers in a list.

marks = [78, 92, 65, 88, 71]


print(sum(marks))

Output:

394
12. max() and min()

max() finds the largest value.

marks = [78, 92, 65, 88, 71]


print(max(marks))

Output:

92

min() finds the smallest value.

print(min(marks))

Output:

65
13. Calculating Average

We can combine sum() and len().

marks = [78, 92, 65, 88, 71]


average = sum(marks) / len(marks)


print("Average:", average)

The pattern is:

Total = sum(list)
Count = len(list)


Average = Total / Count
14. Lists + Conditions

We can use loops and conditions together.

Example:

numbers = [12, 7, 4, 19, 22, 8, 15, 30]


for number in numbers:


    if number % 2 == 0:
        print(number)

Output:

12
4
22
8
30
Important

Don't write:

print(numbers)

inside the loop if you want to print each even number.

Use:

print(number)

because number represents the current item.

15. Building a List with append()

We can start with an empty list:

numbers = []

Then add values one by one.

numbers = []


numbers.append(10)
numbers.append(20)
numbers.append(30)


print(numbers)

Output:

[10, 20, 30]

This becomes very useful when taking multiple inputs from the user.

16. Using a Loop to Build a List

Example:

numbers = []


n = int(input("How many numbers? "))


for i in range(n):


    number = int(input("Enter number: "))
    numbers.append(number)


print(numbers)

If the user enters:

How many numbers? 3
10
20
30

Output:

[10, 20, 30]

This is an important programming pattern:

Create empty list
       ↓
Loop
       ↓
Get input
       ↓
append()
       ↓
Repeat
17. Marks Analyzer

We can use lists to analyze marks.

marks = [78, 92, 65, 88, 71]


print("\n" + "=" * 8, "MARKS ANALYZER", "=" * 8)
print()


print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))


print("=" * 32)

This combines:

list
sum()
len()
max()
min()
18. List Methods You Should Know
Method / Function	Purpose
len(list)	Number of items
list.append(x)	Add to end
list.insert(i, x)	Add at index
list.remove(x)	Remove by value
del list[i]	Remove by index
sum(list)	Total
max(list)	Largest value
min(list)	Smallest value
x in list	Check existence
19. Lists are Mutable

A list can be changed after it is created.

numbers = [10, 20, 30]


numbers[0] = 100


print(numbers)

Output:

[100, 20, 30]

This is called mutability.

Remember:

List → Mutable
String → Immutable

You will learn more about this difference later.

🧪 Day 6 Exercises
Exercise 1 — List Basics

Create a list of your favorite foods.

favorite_foods = ["paneer", "pavbhaji", "shrikhand", "biryani", "gulabjam"]

Print:

Complete list
First food
Last food
Total number of foods

Example:

print(favorite_foods)
print("First food:", favorite_foods[0])
print("Last food:", favorite_foods[-1])
print("Total foods:", len(favorite_foods))
Exercise 2 — Add and Remove

Start with:

fruits = ["apple", "banana", "mango"]

Perform:

fruits.append("orange")
fruits.insert(1, "grapes")
fruits.remove("banana")


print(fruits)

Final list:

['apple', 'grapes', 'mango', 'orange']
Exercise 3 — Marks Analyzer

Create:

marks = [78, 92, 65, 88, 71]

Find:

Total
Average
Highest mark
Lowest mark
Exercise 4 — Even Numbers

Given:

numbers = [12, 7, 4, 19, 22, 8, 15, 30]

Print only the even numbers.

Hint:

for number in numbers:


    if number % 2 == 0:
        print(number)

Expected:

12
4
22
8
30
Exercise 5 — Find a Student

Create:

students = ["Rugved", "Aman", "Rahul", "Priya", "Neha"]

Ask the user for a student name.

student_name = input("Enter student name: ").strip().title()

Then check whether the student exists.

if student_name in students:
    print("Student found!")
else:
    print("Student not found.")
🚀 Day 6 Mini Project — Student Marks Analyzer

Create an empty list and ask the user how many subjects they have.

Then collect marks using a loop.

numbers = []


n = int(input("Enter number of subjects: "))


for i in range(n):


    number = int(input("Enter marks for subject: "))
    numbers.append(number)


print("Marks:", numbers)
print("Total:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Highest:", max(numbers))
print("Lowest:", min(numbers))

Now add a grade system:

average = sum(numbers) / len(numbers)


if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
else:
    print("Grade F")
🧠 Day 6 Problem-Solving Pattern

For programs involving multiple values:

CREATE LIST
     ↓
GET INPUT
     ↓
APPEND VALUES
     ↓
PROCESS LIST
     ↓
CALCULATE
     ↓
DISPLAY RESULT

Example:

numbers = []
     ↓
for loop
     ↓
numbers.append(value)
     ↓
sum / len / max / min
     ↓
average / grade
     ↓
print result

This pattern will become extremely useful when you start working with real-world data.

⚠️ Common Beginner Mistakes
Mistake 1 — Comparing a value with the whole list

Wrong:

if student_name == students:
    print("Student found!")

Correct:

if student_name in students:
    print("Student found!")

== compares two values.

in checks whether a value exists inside a collection.

Mistake 2 — Printing the whole list inside a loop

Wrong:

for number in numbers:


    if number % 2 == 0:
        print(numbers)

This prints the entire list repeatedly.

Correct:

for number in numbers:


    if number % 2 == 0:
        print(number)
Mistake 3 — Forgetting append()

Wrong:

numbers = []


number = int(input("Enter number: "))


# number is not added to the list

Correct:

numbers = []


number = int(input("Enter number: "))


numbers.append(number)
Mistake 4 — Calculating average incorrectly

Don't hard-code the number of values:

average = sum(numbers) / 5

Use:

average = sum(numbers) / len(numbers)

This works even when the list contains a different number of values.

🧠 Day 6 Key Takeaways
list = [...]           → Create a list
list[index]            → Access an item
list[-1]               → Last item
len(list)              → Number of items
list.append(x)         → Add item
list.insert(i, x)      → Insert item
list.remove(x)         → Remove item
del list[i]            → Delete by index
x in list              → Check existence
sum(list)              → Total
max(list)              → Highest
min(list)              → Lowest

Important pattern:

numbers = []


for i in range(n):
    value = int(input("Enter value: "))
    numbers.append(value)
🎯 Day 6 Skill

You can now build programs that:

Store → Add → Remove → Search → Loop → Analyze → Calculate

You built:

List Basics
Add and Remove program
Marks Analyzer
Even Number Filter
Student Search
Student Marks Analyzer

Lists are one of the most important Python concepts, because they are the foundation for handling collections of data.

🚀 Progress
 Day 1 — Python Basics
 Day 2 — Data Types & Operators
 Day 3 — Conditions & Decision Making
 Day 4 — Loops
 Day 5 — Strings & Text Processing
 Day 6 — Lists
 Day 7 — Tuples & Sets
