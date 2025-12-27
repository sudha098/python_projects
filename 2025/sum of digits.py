value = int(input("Enter the value for sum of digits:\n"))

sum_digits = 0
while value > 0:
    sum_digits += value % 10
    value //= 10

print("Sum of digits:", sum_digits)


print("14. Sum of Digits")
num = int(input("Enter a number: "))
sum_digits = sum(int(d) for d in str(num))
print("Sum of digits:", sum_digits, "\n")
