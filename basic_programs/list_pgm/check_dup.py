nums = [1, 2, 3, 4, 5]
duplicate_found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            duplicate_found = True
            break

    if duplicate_found:
        break

print(duplicate_found)

