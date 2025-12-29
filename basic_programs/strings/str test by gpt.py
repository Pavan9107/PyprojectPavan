#Input: "Hello World"
#Output: 3

# count vowels
"""
s = "Hello World"
vowels = 'aeiou'
count = 0
for i in s:
    if i in vowels:
        count += 1

print(count)

#palindrome
s = "racecar"
d = s[::-1]
if s == d:
    print("true")
else:
    print("false")

#Capitalize first letter of each word (without title())
s = "hello world from python"
result =  ""
for i in range(len(s)):
    if i == 0 or s[i-1] == ' ':
        result += s[i].upper()
    else :
        result += s[i]

print(result)

s = "hello world from python"
words = s.split()
capitalized_words = [word[0].upper() + word[1:] for word in words]
result = ' '.join(capitalized_words)
print(result)  # Hello World From Python

s= "hello world"
d = s.replace(" ","")
print(d)

max_count  = 0
max_char = ''

for char in d:
    count = d.count(char)    # count how many times this character appears
    if count > max_count:    # is this a new maximum?
        max_count = count    # update the max count
        max_char = char      # update the max character

print(max_char)
print(max_count)


s = "aabbbccc"

unique_chars = []
char_counts = []

for i in s:
    if i not in unique_chars:
        unique_chars.append(i)
        char_counts.append(s.count(i))

max_count  = max(char_counts)

most_frequent_chars = []

for j in range(len(char_counts)):
    if char_counts[j] == max_count:
        most_frequent_chars.append(unique_chars[j])

print(most_frequent_chars)
print(max_count)



s = "this is python"
l = s.split()
d=[]
print(l)

for i in l:
    d.append(''.join(reversed(i)))

print(d)


s = "This   is    a test"
l = ' '.join(s.split())
print(l)


s = "programming"
d = ""
for i in s:
    if i not in d:
        d += i

print(d)


s = "   hello world   "
d = ' '.join(s.split())
print(d)


s = "Order #1234 will arrive on 2025-08-01"
d = s.replace('#',"").replace('-'," ")
l = d.split()
z= []

for i in range(len(l)):
    if l[i].isdigit():
        z.append(l[i])

print(z)


s = "listen"
d =  "silent"

def check_anagram(s,d):
    if sorted(s) == sorted(d):
        return True
    else:
        return False
print(check_anagram(s,d))


# Implement split() yourself

s = "split this sentence"
d =[]
for i in s:
    d.append(i)
    if i == ' ':
        continue

e = ' '.join(d)
print(e)
"""


s = "hello world hello"
words = s.split()

unique_words = []
counts = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
        counts.append(1)
    else:
        index = unique_words.index(word)
        counts[index] += 1

# Combine into dictionary-like output
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {counts[i]}")



