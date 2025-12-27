value = int(input("Enter the number to check if Armstrong number or not:\n"))
number = str(value)
num_of_digits= len(number)

sum_of_digits = sum(int(digit)**num_of_digits for digit in number)

if value == sum_of_digits:
    print(f"{value} is an Armstrong number.\n")
else:
    print(f"{value} is NOT an Armstrong number.\n")
