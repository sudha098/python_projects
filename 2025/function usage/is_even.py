def is_even(n):
    if n % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

number = int(input("Enter the number:\n"))
print(is_even(number))

def is_even_test():
    assert is_even(4) == "Number is even"
    assert is_even(5) == "Number is odd"

# run the test
is_even_test()
print("Test Successful")
