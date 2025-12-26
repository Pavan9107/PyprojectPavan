nums = [1, 2, 3, 4]
temp = []

for item in range(len(nums)-1,-1,-1):
    temp.append(nums[item])

print(temp)
