#exercise1 : create a dictonary

student = {"name": "Rohit",
           "age": 17,
            "college": "-",
             "Branch": "Artificial intelligence",
              "city": "pune" }

print(student["name"])
print(student["age"])
print(student["college"])
print(student["Branch"])
print(student["city"])

#exercise2 : update

student = {
    "name": "Rugved",
    "age": 17,
    "marks": 80
}

student["age"] = 18
student["marks"] = 85
student["branch"] = "AI"
for key, value in student.items():
    print(key, ":", value)

#exercise3 : search

student = {
    "name": "Rugved",
    "age": 17,
    "branch": "Computer"
}
information = input("Enter information you want: ")
if information in student:
    print("key exist")
else: 
    print("key doesn't exist")

#exercise4: dictonary loop

marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "Python": 95,
    "Physics": 82
}

for key, value in marks.items():
    print(key, ":", value)