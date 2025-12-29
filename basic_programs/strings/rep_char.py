s = "programming"
seen = ""
for i in s:
    if i not in seen:
        seen = seen + i
    else:
        print(i)
        break