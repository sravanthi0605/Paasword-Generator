import random
import string

print("Random Password Generator")

# User input
length = int(input("Enter password length: "))
use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

# Character set handling
if use_letters == 'y':
    characters += string.ascii_letters
if use_numbers == 'y':
    characters += string.digits
if use_symbols == 'y':
    characters += string.punctuation

# Validation
if characters == "":
    print(" Error: Select at least one character type.")
elif length <= 0:
    print(" Error: Password length must be greater than zero.")
else:
    # Password generation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(" Generated Password:", password)
