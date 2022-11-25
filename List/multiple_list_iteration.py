a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6]

for i, j in zip(a, b):
    print(i, j)

t = len(a)
print("")
for k in range(t):
    print(a[k], b[k])
