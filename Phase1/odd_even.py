
num = []
while True:
    try:
        num = input("Enter your number or q to quit :")
        num = num.lower()
        if num == "q":
             print(f"Thanks for playing !!😊")
             break
        num = int(num)

        if num == 0:
            print("0 is neither odd nor even.")
        elif num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

    except ValueError:
            print("Enter a valid Number !!!!")