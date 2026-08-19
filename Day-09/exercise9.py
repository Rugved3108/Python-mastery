#exercise1 : greeting

# def greet(name):
#     print("Hello", name)

# greet("Rugved")

#exercise2: square

# def square(number):
#     return number ** 2

# result = square(5)
# print(result)

#exercise3: even or odd

# def check_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# result = check_even(10)
# print(result)

# exercise4: maximum

# def find_max(a, b, c):
#     result = max(a, b, c)
#     return result 
# answer = find_max(10, 50, 40)
# print(answer)

# exercise 5: calculate avg

# def calculate_avg(a,b,c):
#     total = a + b + c
#     average = total / 3
#     return average
# result = calculate_avg(40,50,60)
# print(result)

#challenge: STUDENT RESULT SYSTEM using function

def student_info():
    name = input("Enter student name:").strip().title()
    age = int(input("Enter student age: "))
    branch = input("Enter branch: ")

    maths = int(input("Enter Maths marks: "))
    python = int(input("Enter Python marks: "))
    english = int(input("Enter English marks: "))

    student = {
        "name": name,
        "age": age,
        "branch": branch,
        "marks": {
            "Maths": maths,
            "Python": python,
            "English": english
        }
    }
    return student

def calculate_total(student):
    return sum(student["marks"].values())

def calculate_avg(student):
    total = sum(student["marks"].values())
    number_of_sub = len(student["marks"])
    return total/number_of_sub

def find_highest(student):
    return max(student["marks"].values())

def find_lowest(student):
    return min(student["marks"].values())

def check_result(avg):
    if avg >= 50:
        return "Passed"
    else:
        return "Failed"

student = student_info()

total = calculate_total(student)
average = calculate_avg(student)
highest = find_highest(student)
lowest = find_lowest(student)
result = check_result(average)

print()
print("=" * 50)
print("STUDENT RESULT SYSTEM".center(50))
print("=" * 50)

print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])

print("\nMarks:")

for subject, marks in student["marks"].items():
    print(subject, ":", marks)

print("=" * 50)
print("Total:", total)
print("Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Result:", result)
print("=" * 50)