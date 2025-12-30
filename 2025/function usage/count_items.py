def count_items(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    return count
    
my_list = input("Enter the list:\n").split()
print(count_items(my_list))
