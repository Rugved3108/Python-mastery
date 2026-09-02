import password_generator

def main():
    
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        password = password_generator.generate_password(length)
        print("Generated password: ", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
