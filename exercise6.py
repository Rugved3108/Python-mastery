# exercise 1: list basics

# favorite_foods = ["paneer", "pavbhaji", "shrikhand", "biryani", "gulabjam"]

# print("\n" + "=" * 8,"LIST BASICS","=" * 8)
# print()
# print(favorite_foods)
# print("First food: ",favorite_foods[0])
# print("Last food: ",favorite_foods[-1])
# print("Total foods: ",len(favorite_foods))
# print("=" * 30)

# exercise 2: add and remove

# fruits = ["apple", "banana", "mango"]

# fruits.append("orange")
# fruits.insert(1,"grapes")
# fruits.remove("banana")
# print(fruits)

#exercise 3: marks analyzer

# marks = [78, 92, 65, 88, 71]

# print("\n" + "=" * 8,"MARKS ANALYZER","=" * 8)
# print()
# print("=" * 32)
# print("Total:", sum(marks))
# print("=" * 32)
# print("Average:", sum(marks)/len(marks))
# print("Highest:",max(marks))
# print("Lowest:",min(marks))
# print("=" * 32)

#exercise 4: even number

# numbers = [12, 7, 4, 19, 22, 8, 15, 30]

# for number in numbers:
#     if number % 2 == 0:
#          print(number)

#exercise 5: find a student

# students = ["Rugved", "Aman", "Rahul", "Priya", "Neha"]

# student_name = input("Enter student name: ").strip().title()

# if student_name in students:
#     print("Student found!")
# else:
#     print("Student not found.")

#exercise 6: list statistics

numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    number = int(input("Enter number: "))
    numbers.append(number)

print("Numbers:", numbers)
print("Total:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Highest:", max(numbers))
print("Lowest:", min(numbers))