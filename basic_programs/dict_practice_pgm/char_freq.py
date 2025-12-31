text = "interview"

d = {}

for char in text:
    if char not in d:
        d[char] = 1

    else:
        d[char] += 1

print(d)