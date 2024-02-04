#packages
import secrets
import string

def generate_password(length, complexity=3):
    characters = string.ascii_letters + string.digits + string.punctuation

    # Adjust character based on complexity level accordingly
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for i in range(length))
    return password

# Get input for password length from user
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length >= 8:
            break
        else:
            print("Password length must be at least 8 characters. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Generate and display the password to the user
password = generate_password(length)
print("Your desired generated password is:", password)
