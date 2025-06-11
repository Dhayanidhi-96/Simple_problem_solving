var = input("Enter your Word or sentences : ").lower()
vow = ["a","e","i","o","u"]
a = 0
b = 0
for i in var:
    if i.isalpha():
        if i in vow:
            a += 1
            
        else:
            b += 1

print(f" Total vowles : {a}\n Total consonants : {b}")       
    
    
