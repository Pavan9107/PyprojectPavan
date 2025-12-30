d = {'a':1, 'b':2, 'c':1}
rev_d = {}

for key,value in d.items():
    if value not in rev_d:
        rev_d[value] = [key]

    else:
        rev_d[value].append(key)

print(rev_d)