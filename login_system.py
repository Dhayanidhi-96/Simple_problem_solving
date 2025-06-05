users = {}
MAX_ATTEMPTS = 3

while True:
    print("\n------ Login Page ------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter your user ID: ")
        if user_id in users:
            print(f"{user_id} already exists ❌")
        else:
            password = input("Enter your password: ")
            users[user_id] = password
            print(f"{user_id} registered successfully ✅")

    elif choice == "2":
        attempts = 0
        while attempts < MAX_ATTEMPTS:
            user_id = input("Enter your user ID: ")
            password = input("Enter your password: ")

            if user_id in users and users[user_id] == password:
                print("✅ Logged in successfully!")
                break  # Exit login loop
            else:
                attempts += 1
                print(f"❌ Invalid credentials. Attempts left: {MAX_ATTEMPTS - attempts}")

        if attempts == MAX_ATTEMPTS:
            print("🚫 Too many failed attempts. Returning to main menu.")

    elif choice == "3":
        print("✅ Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
