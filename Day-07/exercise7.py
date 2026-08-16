#exercise 1:tuples basic

# student = ("Rugved Sutar","18","Python")

# print("Name: ",student[0])
# print("Age: ",student[1])
# print("Language:",student[2])

#exercise 2:tuple challenge

# numbers = (10, 20, 30, 20, 40, 20)

# print("Number of 20s: ",numbers.count(20))
# print("Position of 40: ",numbers.index(40))

#exercise 3:remove duplicate

# numbers = {10, 20, 10, 30, 20, 40, 30, 50}
# print(sorted(numbers))

#exercise 4:unique words

# sentence = input("Enter sentence: ")
# print(set(sentence.split()))

#exercise 5:common skills

student1 = {"Python", "Git", "HTML", "SQL"}
student2 = {"Python", "Java", "SQL", "C++"}
print("skills both students know: ",student1 & student2)
print("All skills: ",student1 | student2)
print("skills only student 1 knows: ",student1 - student2)