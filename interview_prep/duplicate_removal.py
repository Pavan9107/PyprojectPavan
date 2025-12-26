a=[1,2,2,3,4,5,5,3]

new_list = [a[0]]

# for i in range(1, len(a)):
#     if a[i] != a[i-1]:
#         new_list.append(a[i])

# print(new_list)

non_list = []

for i in range(len(a)-1):
    if a[i]!= a[i+1]:
        non_list.append(a[i])

non_list.append(a[-1])
print(non_list)