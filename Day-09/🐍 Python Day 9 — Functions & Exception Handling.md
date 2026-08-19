# 🐍 Python Day 9 — Functions & Exception Handling

Day 9 Goal: Learn how to divide a program into reusable functions and make programs safer using try/except.

Today you moved from writing code that simply works to writing code that is organized, reusable, and able to handle errors.

## 1. What is a Function?

A function is a reusable block of code designed to perform a specific task.

Instead of writing the same logic repeatedly, we write it once inside a function and call it whenever needed.

Without a function
print(10 + 20)
print(50 + 20)
print(100 + 30)
With a function
def add(a, b):
    return a + b


print(add(10, 20))
print(add(50, 20))
print(add(100, 30))
Main idea
Write once → Reuse many times

## 2. Creating a Function

The keyword used to create a function is:

def

Basic syntax:

def function_name():
    # code

Example:

def greet():
    print("Hello Rugved!")

This only defines the function.

It doesn't execute it yet.

## 3. Calling a Function

To execute the function:

greet()

Complete example:

def greet():
    print("Hello Rugved!")


greet()

Output:

Hello Rugved!
Remember
def greet():
    ↓
Create function


greet()
    ↓
Call/run function

## 4. Parameters

A function can receive information.

def greet(name):
    print("Hello", name)

Here:

name

is a parameter.

Calling:

greet("Rugved")

Here:

"Rugved"

is an argument.

Parameter vs Argument
Parameter → variable in function definition


Argument → actual value passed to function

Example:

def add(a, b):
    return a + b

a and b → parameters

add(10, 20)

10 and 20 → arguments

## 5. Multiple Parameters

Functions can have multiple parameters.

def multiply(a, b):
    return a * b


result = multiply(5, 4)


print(result)

Output:

20

## 6. return

return sends a value back from a function.

Example:

def add(a, b):
    return a + b

Then:

result = add(10, 20)


print(result)

Output:

30
Think of it like this:
add(10, 20)
     ↓
10 + 20
     ↓
  return 30
     ↓
result = 30

## 7. print() vs return

This is one of the most important Day 9 concepts.

print()

Displays something on the screen.

def add(a, b):
    print(a + b)

The function displays the result but doesn't give you a useful returned value.

return

Sends the value back.

def add(a, b):
    return a + b

Now you can do:

result = add(10, 20)


print(result)

And even:

if add(10, 20) > 25:
    print("Large")
Remember:
print() → show the result


return → send the result back

For reusable functions, return is often more useful.

## 8. Function with Conditions

Functions can contain if/else.

def check_even(number):


    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

Use it:

result = check_even(10)


print(result)

Output:

Even

## 9. Function with Multiple Steps

Example:

def calculate_average(a, b, c):


    total = a + b + c
    average = total / 3


    return average

Call:

result = calculate_average(40, 50, 60)


print(result)

Output:

50.0

The function can contain multiple operations before returning the final result.

## 10. Default Parameters

A parameter can have a default value.

def greet(name="Rugved"):
    print("Hello", name)

Calling:

greet()

Output:

Hello Rugved

But:

greet("Aman")

Output:

Hello Aman

So:

No argument → default value


Argument provided → provided value

## 11. Returning Multiple Values

Python can return multiple values.

def calculate(a, b):


    total = a + b
    difference = a - b


    return total, difference

Then:

total, difference = calculate(20, 10)


print(total)
print(difference)

Output:

30
10

## 12. Functions Can Work With Lists

You can pass a list to a function.

def calculate_total(numbers):
    return sum(numbers)

Then:

marks = [80, 90, 75, 85]


total = calculate_total(marks)


print(total)

Output:

330

## 13. Functions Can Work With Dictionaries

This connects directly to your Day 8 Student Information System.

def show_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])

Then:

student = {
    "name": "Rugved",
    "age": 17
}


show_student(student)

Output:

Name: Rugved
Age: 17

## 14. Breaking Big Programs Into Functions

Suppose you have a Student Result System.

Instead of one huge block of code:

Student Result System
        ↓
100 lines of code

Break it into smaller tasks:

Student Result System
        │
        ├── get_student_info()
        │
        ├── calculate_total()
        │
        ├── calculate_average()
        │
        ├── find_highest()
        │
        ├── find_lowest()
        │
        └── check_result()

This makes the program:

easier to understand
easier to test
easier to debug
easier to modify
reusable

## 15. Example — Student Result Functions
Get information
def get_student_info():
    name = input("Enter student name: ").strip().title()
    age = int(input("Enter student age: "))
    branch = input("Enter branch: ")


    return {
        "name": name,
        "age": age,
        "branch": branch
    }
Calculate total
def calculate_total(student):
    return sum(student["marks"].values())
Calculate average
def calculate_average(student):
    total = calculate_total(student)
    number_of_subjects = len(student["marks"])


    return total / number_of_subjects
Find highest
def find_highest(student):
    return max(student["marks"].values())
Find lowest
def find_lowest(student):
    return min(student["marks"].values())
Check result
def check_result(average):


    if average >= 50:
        return "Passed"
    else:
        return "Failed"

## 16. Functions + Loops

Functions can be used with loops.

def print_numbers():


    for i in range(1, 6):
        print(i)

Call:

print_numbers()

Output:

1
2
3
4
5

This is important because functions don't replace loops or conditions.

They organize them.

## 17. What Problem Does try/except Solve?

Now we move to the second major part of Day 9.

Consider:

age = int(input("Enter age: "))

If the user enters:

17

Everything works.

But if they enter:

abc

Python can't convert "abc" into an integer.

You get:

ValueError

And the program stops.

## 18. What is Exception Handling?

Exception handling allows your program to handle certain errors instead of crashing.

The main keywords are:

try
except

Basic structure:

try:
    # code that might cause an error


except:
    # what to do if error occurs

## 19. try/except Example
try:
    number = int(input("Enter a number: "))


except ValueError:
    print("Please enter a valid number.")

If the user enters:

25

→ works normally.

If the user enters:

hello

→ ValueError occurs → except handles it.

## 20. Why Specify ValueError?

You could technically write:

except:

But this is usually not a good habit for beginners or production code.

Better:

except ValueError:

because you're saying:

"I specifically know how to handle this type of error."

Example:

try:
    age = int(input("Enter age: "))


except ValueError:
    print("Age must be a number.")

## 21. continue With try/except

This was used in your calculator.

while True:


    try:
        number = float(input("Enter number: "))


    except ValueError:
        print("Invalid number!")
        continue

If invalid input occurs:

input
 ↓
ValueError
 ↓
except
 ↓
print error
 ↓
continue
 ↓
restart loop

## 22. break vs continue

You learned both today in the calculator.

break

Stops the loop completely.

while True:


    choice = input("Continue? ")


    if choice == "no":
        break

Flow:

while
 ↓
break
 ↓
EXIT LOOP
continue

Skips the current iteration and starts the next one.

while True:


    try:
        number = float(input("Number: "))


    except ValueError:
        print("Invalid!")
        continue

Flow:

while
 ↓
continue
 ↓
NEXT ITERATION
Remember:
break    → stop loop


continue → restart next iteration

## 23. Your Calculator Project

Your Day 9 mini project combined:

Functions
+
Parameters
+
Return
+
If / elif / else
+
Input
+
Loops
+
Break
+
Continue
+
Try / except
+
Error handling

That's a major milestone compared with your Day 1 programs.

## 24. Calculator Functions

Your calculator had:

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"


    return a / b

You also added:

def power(a, b):
    return a ** b
def mod(a, b):
    return a % b

and floor division:

def floor_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"


    return a // b

## 25. Calculator Main Loop

The basic structure was:

while True:


    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


    except ValueError:
        print("Invalid number!")
        continue


    operation = input("Enter operation: ")


    if operation == "+":
        result = add(num1, num2)


    elif operation == "-":
        result = subtract(num1, num2)


    elif operation == "*":
        result = multiply(num1, num2)


    elif operation == "/":
        result = divide(num1, num2)


    else:
        result = "Invalid operation"


    print("Result:", result)


    again = input("Calculate again? (yes/no): ").strip().lower()


    if again != "yes":
        break

# 26. Important Mistakes You Made / Almost Made

These are worth writing in your notes because mistakes teach you what to watch for.

❌ Mistake 1 — Wrong average

You previously wrote something like:

print("Average: ", maths + python + english/3)

This is wrong because Python follows operator precedence.

It calculates:

maths + python + (english / 3)

instead of:

(maths + python + english) / 3
Better:
total = maths + python + english
average = total / 3

Or:

average = (maths + python + english) / 3

## 27. ❌ Mistake 2 — max() and min() Without Arguments

You initially tried:

max()
min()

These functions need values.

Correct:

max(maths, python, english)

Or with your dictionary:

max(student["marks"].values())

## 28. ❌ Mistake 3 — Dividing by the Wrong Number

You initially had:

total / 4

when there were only 3 subjects.

Instead of hardcoding:

average = total / 3

you later improved it:

number_of_subjects = len(student["marks"])
average = total / number_of_subjects
This is better programming.

If you later add:

Physics
Chemistry

you don't have to change the calculation.

## 29. ❌ Mistake 4 — Recreating the Dictionary

You initially created student twice.

First:

student = {
    ...
}

Then created it again after getting marks.

The second dictionary replaced the first one.

The better approach is to collect the information first, then create the final dictionary once.

## 30. ❌ Mistake 5 — Writing Everything in One Big Block

Your Student Information System originally had everything together.

Then you learned to separate it into functions.

Instead of:

100-line program

you can have:

get_student_info()
calculate_total()
calculate_average()
find_highest()
find_lowest()
check_result()

This is a major programming skill.

## 31. ❌ Mistake 6 — Forgetting return

Wrong:

def add(a, b):
    a + b

Nothing is returned.

Correct:

def add(a, b):
    return a + b

## 32. ❌ Mistake 7 — Confusing print() and return

Wrong mindset:

def add(a, b):
    print(a + b)

If you need to use the result elsewhere, prefer:

def add(a, b):
    return a + b

Then:

result = add(10, 20)

## 33. ❌ Mistake 8 — Putting Functions Inside the Loop

Avoid:

while True:


    def add(a, b):
        return a + b

The function definitions don't need to be recreated every time.

Better:

def add(a, b):
    return a + b




while True:
    ...
Structure:
FUNCTION DEFINITIONS
        ↓
      MAIN
        ↓
      LOOP
## 34. ❌ Mistake 9 — Forgetting to Handle Division by Zero

This:

def divide(a, b):
    return a / b

will fail when:

divide(10, 0)

Better:

def divide(a, b):


    if b == 0:
        return "Cannot divide by zero"


    return a / b

You should also handle zero for:

%
//

because these operations also cannot use zero as the divisor.

## 35. ❌ Mistake 10 — Using except Too Broadly

Avoid:

try:
    ...
except:
    print("Something went wrong")

when you know the specific error.

Prefer:

except ValueError:

This makes your program easier to understand and debug.

## 36. Function Design Principle

A good function should generally have one clear responsibility.

Good:

def calculate_total(student):
    ...

Good:

def calculate_average(student):
    ...

Less ideal:

def do_everything():
    # get input
    # calculate total
    # print result
    # check result
    # save file
    # ...

Think:

One function → one main job.

## 37. Your Day 9 Mental Model

You should now think about programs like this:

                 PROGRAM
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      FUNCTIONS             MAIN
          │                   │
    ┌─────┼─────┐             ↓
    ↓     ↓     ↓          INPUT
   add   sub   divide         ↓
    │     │     │         CONDITIONS
    └─────┼─────┘             ↓
          ↓                 LOOP
       RETURN                 ↓
          │              OUTPUT
          ↓
       RESULT

And when something can go wrong:

Potential error
      ↓
    try
      ↓
   error?
   /    \
 YES     NO
 ↓       ↓
except  continue

# 🧪 Day 9 Exercises
## Exercise 1 — Greeting
greet(name)

Print a greeting.

## Exercise 2 — Square
square(number)

Return the square.

## Exercise 3 — Even/Odd
check_even(number)

Return "Even" or "Odd".

## Exercise 4 — Maximum
find_max(a, b, c)

Return the largest number.

## Exercise 5 — Average
calculate_average(a, b, c)

Return the average.

# 🚀 Day 9 Mini Projects
# Project 1 — Student Result System

You built this using:

dictionaries
nested dictionaries
functions
return
sum()
len()
max()
min()
conditions
# Project 2 — Calculator

You built a calculator supporting:

+
-
*
/
**
%
//

and added:

Functions
Loop
Error handling
Division-by-zero protection
Invalid operation handling
# 🧠 Day 9 Cheat Sheet
## Function
def greet():
    print("Hello")




## Parameter
def greet(name):
    print("Hello", name)




## Argument
greet("Rugved")




## Return
def add(a, b):
    return a + b




## Store returned value
result = add(10, 20)




## Condition inside function
def check(number):
    if number > 0:
        return "Positive"
    else:
        return "Negative"




## Default parameter
def greet(name="Rugved"):
    print(name)




## Try/except
try:
    number = int(input("Enter number: "))


except ValueError:
    print("Invalid number")




## While loop
while True:
    ...




## Break
break




## Continue
continue
## 🎯 What You Should Be Able to Do After Day 9

Without looking at notes, you should be able to:

Create a function
Pass arguments
Use parameters
Return values
Explain print() vs return
Use functions with lists and dictionaries
Break a large problem into functions
Use while with functions
Use break and continue
Understand try/except
Handle ValueError
Protect calculations from invalid input
Build a basic calculator using functions
🔥 The Biggest Lesson of Day 9

Day 1 taught you:

How to write Python code.

Day 9 is teaching you:

How to organize Python code.

That's a big difference.

Your progression is now:

Day 1
Variables
   ↓
Day 2
Types & Operators
   ↓
Day 3
Conditions
   ↓
Day 4
Loops
   ↓
Day 5
Strings
   ↓
Day 6
Lists
   ↓
Day 7
Collections
   ↓
Day 8
Dictionaries
   ↓
Day 9
Functions + Error Handling

And your calculator project is your first project that genuinely combines many of these concepts together.

Day 9 = Functions + return + try/except + combining concepts. 🐍🔥