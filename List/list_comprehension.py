mylist = []

for i in range(1, 101):
    mylist.append(i)
print(mylist)

mylist = [i for i in range(1, 101)]
print(mylist)

mylist = [i for i in range(1, 101) if i % 2 == 0]
print(mylist)

name="sudhaverma"
mylist=[i for i in name]
print(mylist)

