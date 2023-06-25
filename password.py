import random
import string

def generate_password(length):
    # Define characters to be used in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters to choose from
    characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password
    password = random.choices(characters, k=length)

    # Convert the password list to a string
    password = ''.join(password)

    return password

password_length = int(input("Enter the password length of your choice"))
random_password = generate_password(password_length)
print("Your random Password:", random_password)
