nums = [10, 45, 23, 89, 12]

largest_num = nums[0]

for num in nums:
    if num > largest_num:
        largest_num = num

print(largest_num)