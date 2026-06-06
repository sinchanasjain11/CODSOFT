

import random
import string

print("Welcome to Password Generator!")

length = int(input("Enter password length: "))

print("\nWhat do you want in your password?")
letters = input("Include letters? (yes/no): ").lower()
numbers = input("Include numbers? (yes/no): ").lower()
symbols = input("Include symbols? (yes/no): ").lower()

characters = ""

if letters == "yes":
    characters += string.ascii_letters

if numbers == "yes":
    characters += string.digits

if symbols == "yes":
    characters += string.punctuation

if characters == "":
    print("You did not select anything!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    print("\nYour Generated Password is:")
    print(password)
