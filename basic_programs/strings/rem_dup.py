s = "aabbccdde"
clean_str = ""

for i in s:
    if i not in clean_str:
        clean_str += i
print(clean_str)
