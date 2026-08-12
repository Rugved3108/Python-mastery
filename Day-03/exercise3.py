
# exercise 1 age checker

age = int(input("Enter your age: "))

if age <= 12:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior.")

#Exercise 2: Grade Checker

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#Exercise 3: even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Exercise 4: LOGIN SYSTEM

correct_username = "Thalapathy"
correct_password = "Vijay@69"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username and password.")
