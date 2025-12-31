text = "automation"
count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1


for ch in text:
    if count[ch] == 1:
        print(ch)
        break