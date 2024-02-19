import random
import string

def generate_password(length):
    # Combine uppercase letters, lowercase letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure at least one uppercase letter, one lowercase letter, and one digit
    password = list(random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits))
    
    # Generate the remaining characters randomly
    for _ in range(length - 3):
        password += ''.join(random.choice(characters))
    
    # Shuffling the characters to make the password more random
    random.shuffle(password)
    passw = ''.join(password)
    
    return passw

# taking user input for length of password
length = int(input("Enter the desired length for the password in numbers: "))
print("Generated Password:", generate_password(length))
