a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            print(a[i])
            break