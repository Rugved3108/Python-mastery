print("=" * 34)
print("" * 12,"STUDENT MARKS MANAGER","" * 12)
print("=" * 34)
print()
marks = []
n = int(input("Enter number of subjects:"))
print()
for i in range(n):
    mark = int(input("Enter marks for subject:"))
    marks.append(mark)

print("\n" + "=" * 34 )
print("" * 12, "RESULT", "" * 12)
print("=" * 34 )


print("marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
average = sum(marks) / len(marks)
print("=" * 34)
if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
else:
    print("Grade F")
print("="* 34)