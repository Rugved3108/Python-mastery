#Mini project

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#Smart Calculator

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter operation(+,-,*,/,%): ").strip()
if operation == "+":
    print("Result: ", first_number + second_number)
elif operation == "-":
    print("Result: ", first_number - second_number)
elif operation == "*":
    print("Result: ", first_number * second_number)
elif operation == "%":
    if second_number != 0:
        print("Result: ", first_number % second_number)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "**":
    print("Result: ", first_number ** second_number)
elif operation == "/":
    if second_number != 0:
        print("Result: ", first_number / second_number)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")