marks = {'math': 90, 'science': 95, 'english': 88}

max_value= 0
max_key = None

for key,value in marks.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)
print(max_value)




