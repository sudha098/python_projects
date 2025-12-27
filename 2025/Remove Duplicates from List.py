lst = list(map(int, input("Enter the numbers").split(',')))
unique_numbers = []
for i in lst:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(unique_numbers)
