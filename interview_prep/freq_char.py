char_str = "ddeffghhk"

count_str = {}


for i in char_str:
    if i in count_str:
        count_str[i] += 1
    else:
        count_str[i] = 1

print(count_str)

