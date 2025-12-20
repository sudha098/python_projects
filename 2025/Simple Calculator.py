print("Simple Calculator")

a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
op = input("Enter operation (+,-,*,/):")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print ("Invalid operation")

