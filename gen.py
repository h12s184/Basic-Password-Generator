import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    
    characters = string.ascii_letters  

    if include_digits:
        characters += string.digits  

    if include_special_chars:
        characters += string.punctuation 


    length = max(1, min(length, len(characters)))


    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    include_digits = input("Include digits (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters (y/n): ").lower() == 'y'

    generated_password = generate_password(password_length, include_digits, include_special_chars)

    print(f"\nGenerated Password: {generated_password}")
