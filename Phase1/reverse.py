num = int(input("Enter your number :"))
a = 0

while num > 0:
    digit = num%10
    a = (a*10) + digit
    num = num//10
print(f"Reverse :{a}")
    