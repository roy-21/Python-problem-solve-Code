# Python Mail Generator Mini Project


# first = input("Emter your first name: ")
# last = input("Enter your last name: ")

# email = first.lower() + "." + last.lower() + "@gamil.com"
# print("Your generated email is: ", email)


import re

def generate_valid_gmail(raw_input: str) -> str:
    """
    Converts a given string to a valid Gmail address.
    - Only allows lowercase letters (a-z), numbers (0-9), dots (.), and underscores (_).
    - Removes invalid characters, multiple consecutive dots/underscores, and trims leading/trailing dots/underscores.
    - Falls back to 'user' if the input is empty after cleanup.
    """
    
    # 1. Lowercase all letters (Gmail address is case-insensitive)
    username = raw_input.lower().strip()

    # 2. Replace any characters other than a-z, 0-9, dot (.), and underscore (_) with an underscore (_)
    username = re.sub(r"[^a-z0-9._]", "_", username)

    # 3. Replace multiple consecutive dots or underscores with a single underscore
    username = re.sub(r"[._]{2,}", "_", username)

    # 4. Remove leading and trailing dots or underscores
    username = username.strip("._")

    # 5. If the username is empty after cleanup, assign a default username 'user'
    if not username:
        username = "user"

    # 6. Return the final email address in the format username@gmail.com
    return username + "@gmail.com"


# -------- Main Program --------
# 1. Take input from the user (you can enter any string)
raw_input = input("Enter a string to generate a valid Gmail address: ")

# 2. Generate the valid Gmail address based on the user input
generated_email = generate_valid_gmail(raw_input)

# 3. Output the generated valid Gmail address
print(f"✅ Your generated Gmail address is: {generated_email}")