lst1 = input("Enter list 1:\n").split()
lst2 = input("Enter list 2:\n").split()

lst1 = [int(x) for x in lst1]
lst2 = [int(x) for x in lst2]

merge_list = lst1 + lst2
print(merge_list)
