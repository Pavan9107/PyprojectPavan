text = "programming"
duplicate_list = []
seen = []

for char in text:
    if char in seen:
        if char not in duplicate_list:
            duplicate_list.append(char)
    else:
        seen.append(char)

print(duplicate_list)
