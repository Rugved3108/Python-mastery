# CALCULATOR

#addition

def add(a,b):
    return a + b

#substraction

def subtract(a,b):
    return a - b

#multiplication

def multiply(a,b):
    return a * b

#division

def divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

#power

def power(a,b):
    return a ** b

#modulus

def mod(a,b):
    return a % b

#floor division

def floor(a,b):
    return a // b

#Main 

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid number! Please enter numbers only.")
        continue
    
    operation = input("Enter operation (+, -, *, /, **, %, //): ")

    if operation == "+":
        result = add(num1, num2)

    elif operation == "-":
        result = subtract(num1, num2)

    elif operation == "*":
        result = multiply(num1, num2)

    elif operation == "/":
        result = divide(num1, num2)

    elif operation == "**":
        result = power(num1, num2)

    elif operation == "%":
        result = mod(num1, num2)

    elif operation == "//":
        result = floor(num1, num2)

    else:
        result = "Invalid operation"

    print("Result: ", result)

    again = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Calculator closed.")
        break

