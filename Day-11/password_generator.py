import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
def generate_password(length):
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password
