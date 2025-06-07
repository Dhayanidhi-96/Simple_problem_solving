while True:
    var = input("Enter a value to check (or type 'exit' to quit): ").lower()
    
    if var == "exit":
        print("👋 Exiting the palindrome checker.")
        break

    reversed_var = ""
    for char in var:
        reversed_var = char + reversed_var

    if var == reversed_var:
        print("✅ It's a palindrome")
    else:
        print("❌ It's not a palindrome")
