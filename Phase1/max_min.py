numbers = list(map(int, input("Enter your numbers separated by space: ").split()))
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")



