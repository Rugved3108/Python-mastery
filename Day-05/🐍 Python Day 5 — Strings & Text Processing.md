# 🐍 Python Day 5 — Strings & Text Processing
## 1. What is a String?

A string is a sequence of characters enclosed inside quotes.

name = "Rugved"
language = "Python"

Examples:

"Hello"
'Python'
"123"
"Python is powerful"

Even "123" is a string because it is inside quotes.

# 2. String Indexing

Every character in a string has an index.

word = "Python"

Index positions:

 P   y   t   h   o   n
 0   1   2   3   4   5

Example:

print(word[0])
print(word[1])

Output:

P
y
Negative Indexing

Python also supports negative indexes.

print(word[-1])

Output:

n

Useful:

word[0]     # First character
word[1]     # Second character
word[-1]    # Last character
word[-2]    # Second last character

# 3. len()

len() returns the number of characters in a string.

word = "Python"


print(len(word))

Output:

6

Example:

name = "Rugved"


print(len(name))

# 4. .strip()

.strip() removes unnecessary spaces from the beginning and end of a string.

name = input("Enter your name: ").strip()

If the user enters:

   Rugved

Python stores:

Rugved

It does not remove spaces between words.

name = "Rugved Sutar"


print(name.strip())

# 5. .lower()

.lower() converts all letters into lowercase.

text = "PYTHON"


print(text.lower())

Output:

python

Useful when comparing user input:

answer = input("Continue? ").strip().lower()


if answer == "yes":
    print("Continuing...")

Now:

YES
Yes
yes

can all be converted to:

yes

# 6. .upper()

.upper() converts all letters into uppercase.

text = "python"


print(text.upper())

Output:

PYTHON

# 7. .title()

.title() capitalizes the first letter of each word.

name = "rugved sutar"


print(name.title())

Output:

Rugved Sutar

Useful with user input:

name = input("Enter your name: ").strip().title()

# 8. Loop Through a String

A for loop can process every character in a string.

text = "Python"


for char in text:
    print(char)

Output:

P
y
t
h
o
n

Each character is processed one at a time.

# 9. in Operator

The in operator checks whether something exists inside a string.

text = "python"


if "p" in text:
    print("Found")

Output:

Found

Example with vowels:

if char in "aeiou":
    print("Vowel")

# 10. Vowel Counter

We can combine a loop, condition, in, and a counter.

text = input("Enter text: ").lower()


count = 0


for char in text:
    if char in "aeiou":
        count += 1


print("Vowels:", count)

The logic is:

Input
  ↓
Convert to lowercase
  ↓
Check each character
  ↓
Is it a vowel?
  ↓
Yes → count += 1
  ↓
Print count

# 11. String Slicing

Slicing allows us to extract part of a string.

word = "Python"


print(word[0:3])

Output:

Pyt

Syntax:

string[start:stop]

The stop index is excluded.

Examples:

word[:3]     # Pyt
word[2:]     # thon
word[1:4]    # yth

# 12. Reverse a String

We can reverse a string using:

[::-1]

Example:

word = "Python"


print(word[::-1])

Output:

nohtyP

General slicing syntax:

string[start:stop:step]

A step of -1 moves backwards.

# 13. Palindrome

A palindrome reads the same forwards and backwards.

Examples:

madam
level
radar

Python:

word = input("Enter a word: ").strip().lower()


if word == word[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

Important comparison:

word == word[::-1]

# 14. .count()

.count() tells us how many times something appears.

text = "banana"


print(text.count("a"))

Output:

3

Another example:

text = "python is fun and python is powerful"


print(text.count("python"))

Output:

2

# 15. .split()

.split() breaks a sentence into a list of words.

sentence = "Python is very powerful"


words = sentence.split()


print(words)

Output:

['Python', 'is', 'very', 'powerful']

We can count the number of words:

print(len(sentence.split()))

# 16. Character Frequency

We can count how many times a particular character appears.

text = input("Enter text: ").lower()
character = input("Enter character: ").lower()


count = 0


for char in text:
    if char == character:
        count += 1


print(character, "appears", count, "times")
Important

Don't write:

if char in "character":

because "character" is a string.

Instead:

if char == character:

Here character is the variable containing the user's input.

# 17. Text Analyzer Mini Project
sentence = input("Enter a sentence: ").strip()


print("\n" + "=" * 8, "TEXT ANALYZER", "=" * 8)
print()


print("Characters:", len(sentence))
print("Words:", len(sentence.split()))
print("Python occurrences:", sentence.lower().count("python"))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Reversed:", sentence[::-1])


print("=" * 32)
Concepts used
input()
strip()
len()
split()
lower()
upper()
count()
slicing

# ⚠️ Common Mistakes
Mistake 1 — Confusing a variable with a string

Wrong:

if char in "character":

Correct:

if char == character:
Mistake 2 — Forgetting .lower()

This comparison:

text = "Python"


if "python" in text:
    print("Found")

will not find "python" because uppercase P and lowercase p are different.

Better:

text = input("Enter text: ").lower()


if "python" in text:
    print("Found")
Mistake 3 — Confusing indexing and slicing
word[0]

gets one character.

word[0:3]

gets a section of the string.

# 🧠 Day 5 Key Takeaways
text[0]          → First character
text[-1]         → Last character
len(text)        → Length
text.strip()     → Remove outer spaces
text.lower()     → Lowercase
text.upper()     → Uppercase
text.title()     → Title Case
text.count("a")  → Count occurrences
text.split()     → Split into words
text[::-1]       → Reverse
"a" in text      → Check existence
text[1:4]        → Slicing

# 🎯 Day 5 Problem-Solving Pattern

When solving text-processing problems:

INPUT
  ↓
CLEAN
  ↓
TRANSFORM
  ↓
LOOP / CHECK
  ↓
CALCULATE
  ↓
OUTPUT

For example, a vowel counter:

Input
  ↓
lower()
  ↓
for each character
  ↓
check condition
  ↓
count
  ↓
print result

# 📝 Day 5 Exercises
Exercise 1 — Character Inspector
word = input("Enter a word: ")


print("First character:", word[0])
print("Last character:", word[-1])
print("Length of the word:", len(word))
Exercise 2 — Name Formatter
name = input("Enter your first name: ").strip().title()


print(name)
Exercise 3 — Vowel Counter
text = input("Enter text: ").lower()


count = 0


for char in text:
    if char in "aeiou":
        count += 1


print("Vowels:", count)
Exercise 4 — Reverse Checker
word = input("Enter a word: ").strip().title()


print("Original:", word)
print("Reversed:", word[::-1])
Exercise 5 — Palindrome Checker
word = input("Enter a word: ").strip().lower()


if word == word[::-1]:
    print("Palindrome:", "Yes")
else:
    print("Palindrome:", "No")
Exercise 6 — Character Frequency
text = input("Enter text: ").strip()
character = input("Enter character: ").lower()


count = 0


for char in text:
    if char == character:
        count += 1


print(character, "appears", count, "times")

# 🚀 Day 5 Skill

You can now build programs that:

Input → Clean → Process Text → Check → Count → Output

You built:

Character Inspector
Name Formatter
Vowel Counter
Reverse Checker
Palindrome Checker
Character Frequency Counter
Text Analyzer

This is your next major step toward writing programs that can process and understand text.
