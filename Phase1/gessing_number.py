import random
secret_num = random.randint(1,10)
attempts = 0
while True:
    your_num = int(input("Enter your guessed number:"))
    attempts += 1
    if your_num > secret_num:
        print("Too high !!")
    elif your_num < secret_num:
        print("Too low !!")
    else:
        print(f"correct you gessed it in {attempts} attempts 😉✅")
        break