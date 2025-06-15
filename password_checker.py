import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Check for both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
        return False
    
    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
        return False
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        print(" Password must contain at least one digit.")
        return False
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password must contain at least one special character (!@#$%^&* etc.)")
        return False
    
    # If all checks passed
    return True


def main():
    password = input("Enter your password to check strength: ")
    if check_password_strength(password):
        print("Password is strong!")
    else:
        print("Password is weak. Please try again.")

if __name__ == "__main__":
    main()
