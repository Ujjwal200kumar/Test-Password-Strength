import re

def check_password_strength(password):
    # Define criteria
    min_length = 8
    max_length = 20
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = r'[!@#$%^&*()_+={}\[\]:;<>,.?/~`]'

    # Check length
    if len(password) < min_length or len(password) > max_length:
        return "Password length should be between {} and {} characters.".format(min_length, max_length)

    # Check for uppercase, lowercase, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif re.match(special_chars, char):
            has_special_char = True

    # Check if all criteria are met
    if not has_uppercase:
        return "Password should contain at least one uppercase letter."
    elif not has_lowercase:
        return "Password should contain at least one lowercase letter."
    elif not has_digit:
        return "Password should contain at least one digit."
    elif not has_special_char:
        return "Password should contain at least one special character."
    else:
        return "Password is strong."

# Example usage
password = "StrongPassword123@"
result = check_password_strength(password)
print(result)
