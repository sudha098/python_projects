print("Fibbonachi Series")
n_terms = 5
a = 0
b = 1
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
    print("\n")
