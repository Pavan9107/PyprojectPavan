nums = [3, 5, 4, 3, 5]
found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(nums[i])
            found = True
            break
    if found:
        break
