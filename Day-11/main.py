#EXERCISE 4:YOUR OWN MODULE
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

