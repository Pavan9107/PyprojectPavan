nums = [1, 2, 3, 4, 5, 6]

d = {}

for i in nums:
    if i%2 == 0:
        key = "even"
    else:
        key = "odd"

    if key not in d:
        d[key] = [i]

    else:
        d[key].append(i)

print(d)
