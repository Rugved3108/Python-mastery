#Duplicate Remover

numbers = []
values =input("Enter number: ").split()
for value in values:
    numbers.append(int(value))

print("\n" + "="* 60)
print("DUPLICATE REMOVER".center(60))
print("="*60)
print()

print("Original numbers:", numbers)
unique_numbers = set(numbers)
print("Unique numbers: ",unique_numbers)

print()
print("Original count:", len(numbers))
print("Unique count:", len(unique_numbers))
print("Duplicates removed: ", len(numbers) - len(unique_numbers))

print("="*60)