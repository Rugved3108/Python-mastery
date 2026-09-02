#exercise 1: math

# import math 

# number = float(input("Enter a number: "))
# print("Square root: ", math.sqrt(number))
# print("Ceiling value: ", math.ceil(number))
# print("Floor value: ", math.floor(number))

#exercise 2: random

# import random

# number = random.randint(1,100)
# print("Random number between 1 and 100: ", number)

#exercise 3: random dice

# import random

# number = random.randint(1,6)
# print(number)

#EXERCISE 4:YOUR OWN MODULE
#calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

if __name__ == "__main__":
    print("Calculator module loaded successfully.")

#main.py
import calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = calculator.add(num1, num2)
elif operation == "-":
    result = calculator.subtract(num1, num2)
elif operation == "*":
    result = calculator.multiply(num1, num2)
elif operation == "/":
    result = calculator.divide(num1, num2)
else:
    print("Invalid operation.")
    exit()

print("Result: ", result)