def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n in (0,1):
        return 1
    return factorial(n-1)*n

number  = int(input("Enter number for factorial:\n"))
print(f"Factorial of {number} is: {factorial(number)}")
