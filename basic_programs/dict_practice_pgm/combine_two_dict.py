d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {}

for key,values in d1.items():
    d3[key]=values

for key,values in d2.items():
    if key in d3:
        d3[key]=d3[key]+values
    else:
        d3[key]=values
print(d3)


