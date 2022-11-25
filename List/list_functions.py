mylist = [1, 2, 3, 4, 5, 6]

print(mylist)

del mylist[3]
print(mylist)

mylist.pop(2)
print(mylist)

mylist.remove(6)
print(mylist)

mylist.clear()
print(mylist)

mylist.insert(1, 10)
print(mylist)

newlist = [99, 88]

mylist.append(newlist)
print(mylist)

newlist2 = [9, 8]

mylist.extend(newlist2)
print(mylist)

