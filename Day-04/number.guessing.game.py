#Number Guessing Game

secret_number = 7
while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
