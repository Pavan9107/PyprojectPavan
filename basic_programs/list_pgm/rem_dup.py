nums = [1, 2, 2, 3, 4, 4, 5]
final = []

for item in nums:
    if item not in final:
        final.append(item)

print(final)