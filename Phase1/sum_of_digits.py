num = int(input("Enter your Number : "))
a = 0

while num > 0:
    digit  = num%10
    a += digit
    num = num//10

print(f"Sum of digits {a}")