lst=input("Enter the list of numbers:\n").split()

number = [int(x) for x in lst]

largest = number[0]
for i in number:
    if i > largest:
        largest = i
print(largest)
