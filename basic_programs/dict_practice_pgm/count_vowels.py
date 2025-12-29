s = "interview preparation"
final_count = {}

for char in s:
    if char in "aeiouAEIOU":
        if char in final_count:
            final_count[char] += 1
        else:
            final_count[char] = 1

print(final_count)

max_value = 0
max_vowel = None

for key,value in final_count.items():
    if value > max_value:
        max_value = value
        max_vowel = key

print(max_vowel,max_value)

print(final_count)

max_value = 0

for value in final_count.values():
    if value > max_value:
        max_value = value

for key,value in final_count.items():
    if value == max_value:
        print(key,value)




