import random
import string

def generate_smooth_password(length=16, include_numbers=True, include_special=True):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Limit special characters to a few for a smoother password
    if include_special:
        special_chars = "!@#$%^&*()"

    # Build the allowed character set based on user preferences
    allowed_chars = lower + upper
    if include_numbers:
        allowed_chars += digits
    if include_special:
        allowed_chars += special_chars

    # Generate the password ensuring it's visually smooth
    password = []

    # Add one character from each category to ensure diversity
    if include_numbers:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special_chars))
    password.append(random.choice(lower))
    password.append(random.choice(upper))

    # Fill the rest of the password length with random choices from allowed_chars
    password += random.choices(allowed_chars, k=length - len(password))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list into a string
    return ''.join(password)

# Main Program
print("Welcome to the Smooth Password Generator!")

while True:
    # Ask if the user wants to customize their password or use the default generator
    customize = input("Do you want to create a custom password? (yes/no): ").strip().lower()

    # Check if user entered any form of 'yes'
    if customize in ['yes', 'y']:
        # Ask the user for the password length and preferences
        while True:
            try:
                length = int(input("Enter the desired password length (minimum 12): "))
                if length < 12:
                    print("Password length should be at least 12 characters. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

        include_numbers = input("Include numbers (yes/no): ").strip().lower() in ['yes', 'y']
        include_special = input("Include special characters (yes/no): ").strip().lower() in ['yes', 'y']
    else:
        # Default length for a quick password generation if no customization
        length = 16
        include_numbers = True
        include_special = True

    # Generate three suggested passwords
    passwords = [generate_smooth_password(length, include_numbers, include_special) for _ in range(3)]
    
    print("\nYour generated passwords are:")
    
    # Add a line before the first password
    print('-' * 30)
    
    # Print each password separated by a line
    for pwd in passwords:
        print(f"{pwd}\n{'-' * 30}")  # A line of dashes separating each password
    
    # Ask if the user wants to continue generating passwords
    continue_choice = input("\nDo you want to generate another set of passwords? (yes/no): ").strip().lower()
    
    # If the user chooses 'no' or any form of 'no', break the loop and end
    if continue_choice in ['no', 'n']:
        print("\nGoodbye! Visit my GitHub: https://github.com/waelzaafouri")
        break
