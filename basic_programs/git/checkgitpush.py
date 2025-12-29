"""
a = 'pavan'
b = 'kamal'
c = 'chelli'

l = [a, b, c]

d = ' '.join(l)
print(d)

print(a + " "+ b + " "+ c + " ")

m = d.replace('a','*')
print(m)

"""

s = '(Madam!@' #remove unnecessary characters check if it is palindrome
#m = s.replace('(!@',' ') # this doesnot work as it treats this as (!@' exact substring and it wont find so nothing to replcase
"""
cleaned = ' '
for i in s:
    if i.isalnum():
        cleaned += i.lower()

print(cleaned.strip())

cleaned = 'mellow'

if cleaned == cleaned[::-1]:
    print('palindrome')
else:
    print('not palindrome')

import re
s = " A man from a canal ! @ # \n"
cleaned = re.sub(r'[^a-zA-Z0-9]','',s.lower())
print(cleaned)




d = 'aabbccdd' #check unique and find unique highest substring

unique = ''
count = 0

for i in d:
    if i not in unique:
        unique += i
        count += 1

print(unique)
print(count)



d = 'aabbccdd'
    #01234567
substring = set()

for i in range(len(d)):
    for j in range(i+1, len(d)+1):
        substring.add(d[i:j])

print(substring)
#i=0,
#j=1,2,3,4,5,6,7

d = 'aabbccdd'
unique_substring = []

for i in range(len(d)):
    for j in range(i+1, len(d)+1):
        substring=d[i:j]
        if substring not in unique_substring:
            unique_substring.append(substring)
print(unique_substring)

def test():
    for i in range(10):
        return i

print(test())

"""






