# 🐍 Python Day 10 — File Handling
## 🎯 Day 10 Goal

Today we learned how to make Python programs store data permanently using files.

Until now, most of our programs worked like this:

Program starts
      ↓
User enters data
      ↓
Program runs
      ↓
Program closes
      ↓
Data is lost ❌

With file handling:

Program starts
      ↓
User enters data
      ↓
Python saves data to a file
      ↓
Program closes
      ↓
Data remains ✅

## 1. What is File Handling?

File handling means using Python to:

create files
write data
read data
add data
modify/manage stored information

For example:

notes.txt
students.txt
users.txt
history.txt

Files allow our programs to store information beyond a single execution.

## 2. Opening a File

Python uses the open() function.

Basic syntax:

file = open("filename.txt", "mode")

Example:

file = open("notes.txt", "r")

Here:

notes.txt → file name
r         → file mode

## 3. File Modes

The three important modes we learned are:

Mode	Meaning	Main purpose
"r"	Read	Read existing data
"w"	Write	Write/replace data
"a"	Append	Add data to the end
Easy way to remember:
r → read
w → write
a → add

## 4. "r" — Read Mode

Used to read an existing file.

with open("notes.txt", "r") as file:
    content = file.read()

print(content)

"r" means:

Open this file so I can read its contents.

If the file doesn't exist, Python can raise:

FileNotFoundError

## 5. "w" — Write Mode

Used to write data into a file.

with open("notes.txt", "w") as file:
    file.write("Learning Python")

The file will contain:

Learning Python
⚠️ Important

"w" can overwrite existing content.

Suppose the file contains:

Python
Functions
Loops

Then:

with open("notes.txt", "w") as file:
    file.write("File Handling")

The old content is replaced:

File Handling

So remember:

"w" = write fresh/replace existing content.

## 6. "a" — Append Mode

Append means add to the end.

with open("notes.txt", "a") as file:
    file.write("File Handling\n")

If the file previously contained:

Python
Functions

it becomes:

Python
Functions
File Handling

Existing content is preserved.

## 7. close()

When using open() directly:

file = open("notes.txt", "r")

content = file.read()

file.close()

close() closes the file after we're finished using it.

## 8. with open() — Recommended Method

Instead of manually closing:

file = open("notes.txt", "r")

content = file.read()

file.close()

we can use:

with open("notes.txt", "r") as file:
    content = file.read()

Python automatically handles closing the file.

Recommended pattern:
with open("filename.txt", "mode") as file:
    # work with file

This is the style you should normally use.

## 9. Writing to a File

We use:

write()

Example:

with open("notes.txt", "w") as file:
    file.write("Python Day 10")

The file becomes:

Python Day 10

## 10. Writing Multiple Lines

Use \n to create a new line.

with open("notes.txt", "w") as file:
    file.write("Python\n")
    file.write("Functions\n")
    file.write("File Handling\n")

The file becomes:

Python
Functions
File Handling
Remember:
\n → new line

## 11. Writing User Input to a File

We can combine input() and file handling.

name = input("Enter your name: ")

with open("users.txt", "a") as file:
    file.write(name + "\n")

If the user enters:

Rugved

the file contains:

Rugved

If another user enters:

Aman

the file becomes:

Rugved
Aman

because we used "a".

## 12. Reading a File With read()

read() reads the entire file.

with open("notes.txt", "r") as file:
    content = file.read()

print(content)

Think:

File
 ↓
read()
 ↓
Entire content
 ↓
String

## 13. readline()

readline() reads one line at a time.

with open("notes.txt", "r") as file:
    line = file.readline()

print(line)

If the file contains:

Python
Functions
File Handling

the first readline() returns:

Python

## 14. readlines()

readlines() reads all lines and returns them as a list.

with open("notes.txt", "r") as file:
    lines = file.readlines()

print(lines)

You may get:

['Python\n', 'Functions\n', 'File Handling\n']
Difference:
read()       → entire content as a string

readline()   → one line

readlines()  → all lines as a list

## 15. Reading a File Using a Loop

You can loop through the file:

with open("notes.txt", "r") as file:
    for line in file:
        print(line)

This processes the file one line at a time.

Conceptually:

File
 ↓
Line 1 → process
 ↓
Line 2 → process
 ↓
Line 3 → process

This becomes especially useful for larger files.

## 16. try/except With Files

Files can cause errors.

For example:

with open("notes.txt", "r") as file:
    content = file.read()

If notes.txt doesn't exist, Python can raise:

FileNotFoundError

We can handle it:

try:
    with open("notes.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")

Now the program doesn't simply crash.

## 17. Why Use a Specific Exception?

You could write:

except:
    print("Something went wrong")

But this is too broad.

It's better to specify the error you expect:

except FileNotFoundError:

This tells Python:

Handle the situation where the file doesn't exist.

This is a good programming habit.

## 18. Combining Functions + Files

Day 9 taught us functions.

Day 10 taught us files.

Now we combine them.

Example:

def add_note():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

And:

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()

        print(content)

    except FileNotFoundError:
        print("No notes found.")

Now each function has one clear responsibility.

add_note()
    ↓
save note

view_notes()
    ↓
read notes

## 19. Personal Notes App — Our Day 10 Project

We built:

================================
        PERSONAL NOTES APP
================================

1. Add personal notes
2. View personal notes
3. Exit

The user chooses an option.

Option 1

Save a note:

def add_notes():
    notes = input("Enter your personal notes: ").strip()

    with open("personal_notes.txt", "a") as file:
        file.write(notes + "\n")
Option 2

Read notes:

def view_notes():
    try:
        with open("personal_notes.txt", "r") as file:
            content = file.read()

        print("\nYour personal notes:")
        print(content)

    except FileNotFoundError:
        print("\nNo personal notes found. Please add some notes first.")
Option 3

Exit:

break

## 20. Main Menu Structure

The main program uses a while loop:

while True:

    print("1. Add personal notes")
    print("2. View personal notes")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_notes()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

This gives us a menu-driven application.

## 21. Overall Architecture

Your Personal Notes App now looks like:

             PERSONAL NOTES APP
                     │
                 while True
                     │
                  choice
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
     add_notes() view_notes()  exit
          ↓          ↓
       "a" mode    "r" mode
          ↓          ↓
       save data  read data

This is a much better structure than putting everything into one huge block.

## 22. Important Mistakes From Day 10
❌ Mistake 1 — Confusing "w" and "a"

Using:

open("notes.txt", "w")

when you want to keep old notes can cause data to be overwritten.

For adding notes:

open("notes.txt", "a")

is usually appropriate.

❌ Mistake 2 — Forgetting \n

If you write:

file.write("Python")
file.write("Java")

the file may contain:

PythonJava

Instead:

file.write("Python\n")
file.write("Java\n")

gives:

Python
Java
❌ Mistake 3 — Forgetting to close a manually opened file

If you use:

file = open("notes.txt", "r")

you should eventually use:

file.close()

Better:

with open("notes.txt", "r") as file:
❌ Mistake 4 — Reading a file that doesn't exist

This can cause:

FileNotFoundError

Handle it when appropriate:

try:
    ...
except FileNotFoundError:
    ...
❌ Mistake 5 — Saving empty notes

You used:

notes = input("Enter your personal notes: ").strip()

That's good.

But the user can still enter nothing.

A better version:

if notes == "":
    print("Note cannot be empty.")
    return

## 23. return Inside a Function

Here return doesn't necessarily return a value.

It can simply stop the function.

Example:

def add_note():

    note = input("Enter note: ").strip()

    if note == "":
        print("Note cannot be empty.")
        return

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

If the note is empty:

if
 ↓
return
 ↓
function ends

## 24. Day 10 Concepts Combined

You are now combining concepts from multiple days:

Variables
   +
Input
   +
Conditions
   +
Loops
   +
Functions
   +
Strings
   +
Exception Handling
   +
File Handling

This is an important transition.

You're no longer learning isolated Python syntax.

You're starting to build programs.

# 🧠 Day 10 Cheat Sheet
Open file
with open("file.txt", "r") as file:
Read
content = file.read()
Read one line
line = file.readline()
Read all lines
lines = file.readlines()
Write
file.write("Hello\n")
Modes
"r" → Read
"w" → Write/replace
"a" → Append
Handle missing file
try:
    with open("file.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found.")
Recommended file syntax
with open("file.txt", "a") as file:
    file.write("Hello\n")

# 🧪 Day 10 Practice Exercises
## Exercise 1 — Notes File

Ask the user for:

favorite programming language
favorite subject
goal

Save them into notes.txt.

## Exercise 2 — Read Notes

Read notes.txt and display everything.

## Exercise 3 — Add Note

Ask:

Enter another note:

and append it to the file.

## Exercise 4 — File Error Handling

Try to open a file that doesn't exist.

Handle:

FileNotFoundError

without crashing.

# Exercise 5 — Notes App

Build a menu:

1. Add Note
2. View Notes
3. Exit

Use:

functions
while
if/elif/else
files
try/except
🏆 Day 10 Mini Project
Personal Notes App

Features:

✅ Add notes
✅ Save notes permanently
✅ View notes
✅ Append new notes
✅ Handle missing file
✅ Functions
✅ Menu
✅ Loop
✅ Error handling

You completed this project yourself and then improved it with functions and FileNotFoundError handling.

## 🎯 What You Should Know Before Moving to Day 11

Try explaining these without looking at your notes:

### 1. What is the difference between:
"r"
"w"
"a"
### 2. What does this do?
with open("notes.txt", "a") as file:
### 3. What's the difference between:
read()
readline()
readlines()
### 4. Why do we use:
\n
### 5. Why is with open() preferred?
### 6. What happens if we try to read a nonexistent file?
### 7. Why do we use:
try:
    ...
except FileNotFoundError:
    ...
### 8. Why is "a" better than "w" for your notes app?

If you can answer these and rebuild your Personal Notes App without looking at the code, you're ready for Day 11. 🐍🔥