
def prime_number(n):
    if n > 1 and all(n%i!=0 for i in range(2, int(n**0.5)+1)):
        return "Prime number"
    else:
        return "Not prime"
print(prime_number(16))
