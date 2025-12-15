print("Max in list")

nums = [1, 2, 3, 5, 2, 5, 67, 4]

maximum = nums[0]
for n in nums:
    if n > maximum:
        maximum = n

print(maximum)
