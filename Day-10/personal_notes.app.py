# personal notes app

print("=" * 30)
print("PERSONAL NOTES APP".center(30))
print("=" * 30)
print()

def add_notes():
    notes = input("Enter your personal notes: ").strip()
    if notes == "":
        print("Notes cannot be empty. Please enter some notes.")
        return
    with open("personal_notes.txt", "a") as file:
            file.write(notes + "\n")
    print("Notes added successfully!")

def view_notes():
    try:
        with open("personal_notes.txt", "r") as file:
            content = file.read()
        print("\nYour personal notes:")
        print(content)
    except FileNotFoundError:
        print("\nNo personal notes found. Please add some notes first.")

while True:
    print("1. Add personal notes")
    print("2. View personal notes")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        add_notes()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    


 

    







