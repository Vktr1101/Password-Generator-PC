import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    
    characters = string.ascii_letters  
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    
    password = []
    password.append(random.choice(string.ascii_lowercase))  
    password.append(random.choice(string.ascii_uppercase))  

    if use_digits:
        password.append(random.choice(string.digits))       
    if use_symbols:
        password.append(random.choice(string.punctuation))  

    
    while len(password) < length:
        password.append(random.choice(characters))

    
    random.shuffle(password)

    return ''.join(password)



print("=== Password Generator ===")
length = int(input("Enter password length: "))


use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"


password = generate_password(length, use_digits, use_symbols)
print("\nGenerated password:", password)


with open("passwords.txt", "a") as f:
    f.write(password + "\n")

print("Password saved in passwords.txt")
