while True:
    print("\n------ Calculator Menu ------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Please enter valid numbers!")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("🚫 Cannot divide by zero!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2:.2f}")

    elif choice == '5':
        print("✅ Exiting Calculator. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
