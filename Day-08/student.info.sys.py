# student information system

name = input("Enter student name: ").strip().title()
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

print()
print("=" * 50)
print("STUDENT INFO SYSTEM".center(50))
print("="*50)
print()

print("Name: ", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])

print("\nMarks: ")

for subject, marks in student["marks"].items():
     print(subject, ":", marks)

total = sum(student['marks'].values())
number_of_subjects = len(student["marks"])
average = total/number_of_subjects

print("="*50)
print("Total: ",total )
print("Average: ",average )
print("Highest Marks: ", max(student["marks"].values()))
print("Lowest Marks: ", min(student["marks"].values()))
print("=" * 50)
if average >= 50:
     print("Result: Passed")
else:
    print("Result: Failed")
print("=" * 50)