mylist=[1,2,4,6,7,8,9]
lenght=len(mylist)
print(mylist)
print(lenght)

for i in range(lenght):
    print(mylist[i])

print(" ")

for j in mylist:
    print(j)

print(" ")

for k in range(lenght-1,-1,-1):
    print(mylist[k])