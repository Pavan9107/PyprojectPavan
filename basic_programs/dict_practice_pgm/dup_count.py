nums = [1, 2, 3, 2, 1, 4]
count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print(count)

for key, value in count.items():
    if value >1:
        print(key,":",value)

