words = ['apple', 'ant', 'ball', 'bat', 'cat']
d = {}

for word in words:
    first_char = word[0]
    if first_char not in d:
        d[first_char] = [word]

    else:
        d[first_char].append(word)

print(d)