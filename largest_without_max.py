numbers = [10, 50, 20, 80, 40]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number =",largest)