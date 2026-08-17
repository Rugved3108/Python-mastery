# 🐍 Python Day 7 — Tuples & Sets
1. What is a Tuple?

A tuple is a collection of multiple values, similar to a list.

The main difference is:

Lists can be changed, but tuples cannot be changed after creation.

Tuple:

numbers = (10, 20, 30, 40)

List:

numbers = [10, 20, 30, 40]
2. Creating a Tuple

Tuples are usually created using parentheses ().

numbers = (10, 20, 30, 40)


names = ("Rugved", "Aman", "Rahul")


marks = (78, 92, 65)

You can also create a tuple without parentheses:

numbers = 10, 20, 30

But using parentheses makes your code clearer.

3. Tuple Indexing

Tuples use indexing just like lists and strings.

numbers = (10, 20, 30, 40)

Indexes:

10    20    30    40
 0     1     2     3

Example:

print(numbers[0])
print(numbers[2])

Output:

10
30

Negative indexing also works:

print(numbers[-1])

Output:

40
4. Tuple Slicing

Tuples also support slicing.

numbers = (10, 20, 30, 40, 50)


print(numbers[1:4])

Output:

(20, 30, 40)

Other examples:

numbers[:3]     # (10, 20, 30)
numbers[2:]     # (30, 40, 50)
numbers[::-1]   # (50, 40, 30, 20, 10)
5. Tuple is Immutable

Tuples cannot be changed after they are created.

numbers = (10, 20, 30)


numbers[0] = 100

This produces an error.

You cannot use:

numbers.append(40)
numbers.remove(20)

because tuples cannot be modified.

Think:

List
→ Mutable
→ Can change


Tuple
→ Immutable
→ Cannot change
6. Why Use Tuples?

Tuples are useful when you have data that should remain unchanged.

Examples:

coordinates = (19.0760, 72.8777)


rgb = (255, 255, 255)


days = ("Monday", "Tuesday", "Wednesday")

These values generally represent a fixed collection of information.

7. len() with Tuples

Just like lists, len() tells us how many items are in a tuple.

numbers = (10, 20, 30, 40)


print(len(numbers))

Output:

4
8. Loop Through a Tuple

A for loop can process each item.

numbers = (10, 20, 30, 40)


for number in numbers:
    print(number)

Output:

10
20
30
40
9. .count()

.count() tells us how many times a value appears in a tuple.

numbers = (10, 20, 30, 20, 40, 20)


print(numbers.count(20))

Output:

3

So:

numbers.count(20)

means:

Count how many times 20 appears.

10. .index()

.index() tells us the position of the first occurrence of a value.

numbers = (10, 20, 30, 20, 40, 20)


print(numbers.index(40))

Output:

4

Remember:

.index() returns the position, not the value itself.

11. Tuple Challenge
numbers = (10, 20, 30, 20, 40, 20)


print("Number of 20s:", numbers.count(20))
print("Position of 40:", numbers.index(40))

Output:

Number of 20s: 3
Position of 40: 4
12. What is a Set?

A set is a collection of unique values.

Sets are created using {}.

numbers = {10, 20, 30, 40}

Example:

skills = {"Python", "Git", "HTML"}
13. Sets Remove Duplicates

One of the most useful features of sets is that they automatically remove duplicate values.

numbers = {10, 20, 10, 30, 20, 40, 30}


print(numbers)

The result contains each value only once.

Conceptually:

Original:


10 20 10 30 20 40 30


        ↓


Set:


10 20 30 40

This is extremely useful for finding unique values.

14. Sets Are Unordered

Sets do not maintain a reliable index order like lists.

Therefore, this does not work:

numbers = {10, 20, 30}


print(numbers[0])

You should not use indexing with sets.

If you need an ordered collection with indexes, use a list.

15. Creating a Set from a List

You can convert a list into a set.

numbers = [10, 20, 10, 30, 20, 40]


unique_numbers = set(numbers)


print(unique_numbers)

The duplicate values are removed.

This is one of the most useful set patterns:

List
  ↓
set()
  ↓
Unique values
16. len() with Sets

len() tells us how many unique values are inside the set.

numbers = {10, 20, 30, 40}


print(len(numbers))

Output:

4

Example:

numbers = [10, 20, 10, 30, 20, 40]


unique_numbers = set(numbers)


print("Original count:", len(numbers))
print("Unique count:", len(unique_numbers))
17. Adding to a Set

Use .add() to add an item.

skills = {"Python", "Git"}


skills.add("SQL")


print(skills)

Now the set contains:

Python
Git
SQL

If you add an existing value:

skills.add("Python")

the set will still contain only one "Python".

18. Removing from a Set

Use .remove() to remove an item.

skills = {"Python", "Git", "SQL"}


skills.remove("Git")


print(skills)

Now:

Python
SQL
19. Check if an Item Exists

Use in.

skills = {"Python", "Git", "SQL"}


if "Python" in skills:
    print("Python is present.")

Output:

Python is present.

This is similar to checking membership in a list.

20. Set Union |

Union combines all unique values from two sets.

student1 = {"Python", "Git", "HTML"}
student2 = {"Python", "Java", "SQL"}


all_skills = student1 | student2


print(all_skills)

Conceptually:

Student 1:
Python Git HTML


Student 2:
Python Java SQL


        ↓


All:
Python Git HTML Java SQL

Think:

| → Combine sets
21. Set Intersection &

Intersection finds values that exist in both sets.

student1 = {"Python", "Git", "HTML", "SQL"}
student2 = {"Python", "Java", "SQL", "C++"}


common = student1 & student2


print(common)

Result:

Python
SQL

Think:

& → Common values
22. Set Difference -

Difference finds values that exist in the first set but not in the second.

student1 = {"Python", "Git", "HTML", "SQL"}
student2 = {"Python", "Java", "SQL", "C++"}


only_student1 = student1 - student2


print(only_student1)

Result:

Git
HTML

Think:

- → Only in first set
23. Set Operations Summary
A | B
→ Union
→ Everything from both sets


A & B
→ Intersection
→ Common values


A - B
→ Difference
→ Values only in A

Visual idea:

A = {1, 2, 3}
B = {3, 4, 5}


A | B → {1, 2, 3, 4, 5}


A & B → {3}


A - B → {1, 2}
24. Tuple vs List vs Set
Feature	List	Tuple	Set
Syntax	[]	()	{}
Ordered	Yes	Yes	No reliable order
Duplicates	Allowed	Allowed	Removed
Mutable	Yes	No	Yes
Indexing	Yes	Yes	No
Main use	Collection of changeable data	Fixed data	Unique data

Think:

List
→ I need an ordered collection that can change.


Tuple
→ I need a fixed collection.


Set
→ I need unique values.
25. Duplicate Remover

Sets are excellent for removing duplicates.

numbers = []


values = input("Enter numbers: ").split()


for value in values:
    numbers.append(int(value))


print("Original numbers:", numbers)


unique_numbers = set(numbers)


print("Unique numbers:", unique_numbers)


print("Original count:", len(numbers))
print("Unique count:", len(unique_numbers))


print("Duplicates removed:",
      len(numbers) - len(unique_numbers))

Example:

Enter numbers:
10 20 10 30 20 40


Original numbers:
[10, 20, 10, 30, 20, 40]


Unique numbers:
{10, 20, 30, 40}


Original count: 6
Unique count: 4
Duplicates removed: 2
🧪 Day 7 Exercises
Exercise 1 — Tuple Basics

Create a tuple containing:

Your name
Your age
Your favorite programming language

Example:

your_name = "Rugved Sutar"
your_age = 18
your_favorite_programming_language = "Python"


student = (your_name, your_age, your_favorite_programming_language)


print("Name:", student[0])
print("Age:", student[1])
print("Language:", student[2])
Exercise 2 — Tuple Challenge

Given:

numbers = (10, 20, 30, 20, 40, 20)

Find:

Number of times 20 appears
Position of 40

Hint:

numbers.count(20)
numbers.index(40)
Exercise 3 — Remove Duplicates

Given:

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

Convert the list into a set.

unique_numbers = set(numbers)


print(unique_numbers)

Challenge:

Print the unique numbers in sorted order.

print(sorted(unique_numbers))
Exercise 4 — Unique Words

Ask the user to enter a sentence.

Convert it into a set of words.

sentence = input("Enter sentence: ")


words = sentence.split()


unique_words = set(words)


print(unique_words)

This removes repeated words.

Exercise 5 — Common Skills

Create two sets:

student1 = {"Python", "Git", "HTML", "SQL"}
student2 = {"Python", "Java", "SQL", "C++"}

Find:

Common skills
print(student1 & student2)
All skills
print(student1 | student2)
Skills only Student 1 knows
print(student1 - student2)
🚀 Day 7 Mini Project — Duplicate Remover

Build a program that:

Takes multiple numbers from the user
Stores them in a list
Removes duplicates using a set
Displays original values
Displays unique values
Shows original count
Shows unique count
Shows how many duplicates were removed

Starter structure:

numbers = []


values = input("Enter numbers: ").split()


for value in values:
    numbers.append(int(value))


unique_numbers = set(numbers)


print("\n" + "=" * 60)
print("DUPLICATE REMOVER".center(60))
print("=" * 60)


print("Original numbers:", numbers)
print("Unique numbers:", unique_numbers)


print("Original count:", len(numbers))
print("Unique count:", len(unique_numbers))


print("Duplicates removed:",
      len(numbers) - len(unique_numbers))


print("=" * 60)
🧠 Day 7 Problem-Solving Pattern

When you need to work with fixed data:

Create Tuple
    ↓
Access / Read
    ↓
Process
    ↓
Output

When you need unique data:

Input
  ↓
List
  ↓
set()
  ↓
Unique values
  ↓
Process
  ↓
Output

When comparing two groups:

Set A
  ↓
Set Operations
  ↓
Union / Intersection / Difference
  ↓
Result
⚠️ Common Beginner Mistakes
Mistake 1 — Trying to modify a tuple

Wrong:

numbers = (10, 20, 30)


numbers[0] = 100

Tuples cannot be modified.

Mistake 2 — Expecting a set to have indexes

Wrong:

numbers = {10, 20, 30}


print(numbers[0])

Sets do not support indexing.

Mistake 3 — Confusing {} with an empty set

This:

data = {}

creates an empty dictionary, not an empty set.

For an empty set:

data = set()

You will learn dictionaries in a later lesson.

Mistake 4 — Forgetting that sets remove duplicates
numbers = {10, 20, 10, 30}


print(numbers)

You won't get the duplicate 10.

That's actually one of the main purposes of a set.

🧠 Day 7 Key Takeaways
tuple = (1, 2, 3)
→ Fixed collection


set = {1, 2, 3}
→ Unique collection


tuple[index]
→ Access tuple item


tuple.count(x)
→ Count occurrences


tuple.index(x)
→ Find position


set(list)
→ Remove duplicates


A | B
→ Union


A & B
→ Intersection


A - B
→ Difference


x in collection
→ Check membership
🎯 Day 7 Skill

You can now choose the right collection based on the problem:

List → Changeable ordered data

Tuple → Fixed data

Set → Unique data

You built:

Tuple Basics
Tuple Search
Duplicate Remover
Unique Words
Common Skills Analyzer
Duplicate Remover Mini Project

This is an important step because you're moving from simply writing Python statements to choosing the right data structure for a problem.

🚀 Progress
 Day 1 — Python Basics
 Day 2 — Data Types & Operators
 Day 3 — Conditions & Decision Making
 Day 4 — Loops
 Day 5 — Strings & Text Processing
 Day 6 — Lists
 Day 7 — Tuples & Sets
 Day 8 — Dictionaries & Key-Value Data