l =[10, 20, 4, 45, 99]
largest = l[0]
second_largest = float('-inf')

for i in l:
    if i > largest:
        second_largest = largest
        largest = i

    elif i < largest and i > second_largest:
        second_largest = i

print(second_largest)
