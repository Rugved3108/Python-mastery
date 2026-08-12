
# #Challenge

# Name = input("Enter your name: ")
# Maths = int(input("Enter your marks in Maths: "))
# Science = int(input("Enter your marks in Science: "))
# English = int(input("Enter your English marks: "))
# Total = Maths + Science + English
# Average = Total / 3
# print()
# print("Student Report")
# print("-----------------")
# print("Name:", Name)
# print("Maths:", Maths)
# print("Science:", Science)
# print("English:", English)
# print("Total:", Total)
# print("Average:", Average)

#Fun challenge

name =input("Enter your name: ").title()
favorite_programming_language = input("Enter your favorite programming language: ")

current_year = 2026
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

print()
print("\n" + "*" * 20)
print(f"WELCOME {name.upper()}")
print("*" * 20)

print(f"\nHello {name}!")
print()
print(f"You are {age} years old.")
print()
print(f"Your favorite programming language is {favorite_programming_language}.")
print()
print(f"Have a great day ahead!")