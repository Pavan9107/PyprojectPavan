r= [2, 3, 2, 4, 3, 5]
count= {}

for i in r:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

print(count)

for key, value in count.items():
    if value == 1:
        print(key)
        print(value)
        break


