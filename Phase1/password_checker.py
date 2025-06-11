password = input("Enter your password: ")
special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"

has_digit = any(char.isnumeric() for char in password)
has_spcl_char = any(char in special_chars for char in password)
long = len(password) >= 8

if has_digit and has_spcl_char and long:
    print("Strong password ✅")
else :
    print("❌ Weak Password: Must be at least 8 characters and include a digit and special character")
