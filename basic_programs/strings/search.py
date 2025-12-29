"""
log = "User: [john_doe] | Action: login | Time: 14:55"
name  = log.find("[")+1
end = log.find("]")
print(log[name : end])

b = log.split( ' |')
c =b[1].split(' :')
print(c)

url = "www.example.com"
print(url.strip("w."))  # 'example.com'

text = "  Hello   world! Hello everyone. HELLO!!!  "
cleaned = text.lower().strip().replace('!', '').replace('.','').split()
print(cleaned )
print(cleaned.count('hello'))

post = "Loving the new features in #Python3.9! #python #coding #Coding, #100DaysOfCode #python."
d= post.find('#','#')
print(d)


text = "  Hello   world! Hello everyone. HELLO!!!  "
cleaned =  []
for i in text:
    if i.isalnum():
        cleaned.append(i)

#nxtstr = " ".join(cleaned).lower()
print(cleaned)

squares = [x**2 for x in range(10)]
print(squares)

fruits = ["apple", "banana", "cherry", "mango", "grape"]
fruits.append("orange")
fruits.extend("kiwi")
print(fruits)

numbers = [1, 2, 3, 4, 5]
result = []

def squared(nums):
    for n in nums:
        result.append(n ** 2)

squared(numbers)
print(result)

text = "banana"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)  # Output: {'b': 1, 'a': 3, 'n': 2}


import collections
from itertools import count


str = "The quick brown fox jumps over the lazy dog"
b = str.lower().replace(" ","")
print(b)
s= {}

for i in b:
    if i in s:
        s[i] += 1
    else:
        s[i]=1

print(s)

max_count = 0
max_char  = ''

for char,count in s.items():
    if count > max_count:
        max_count = count
        max_char = char

print(max_char,max_count)

max_count = max(s.values())
print(max_count)

def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ","")
    word2 = word2.lower().replace(" ","")

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

print(is_anagram('listen','silent'))

text = "hello"
rev = ""
for i in text:
    rev = i + rev
print(rev)


text = "banana"
count = text.count("ana")
print(count)  # Output: 1 (only one non-overlapping "ana")


def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

print(all_substrings("abc"))


def unique_substrings(s):
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i+1, n+1):
            result.add(s[i:j])
    return result

print(unique_substrings("ababa"))


s="aaabajbaj"
b=" "
for i in range(len(s)):
    b += s[i]
print(b)



s= "abc"
a= list(s)
print(a)

from itertools import combinations
c= list(combinations(a,2))
print(c)

from itertools  import combinations
def all_substrings(s):
    n = len(s)
    result = set()
    for r in range(1,n+1):
        for comb in combinations(s,r):
            result.add(''.join(comb))
    return result
print(all_substrings("abc"))


count = 0
str = "banana"
match = "aeiou"

for i in str:
    if i in match:
        count +=i

print(count)

lst = ["madam", "hello"]

def ceck_palind(lst):
    for i in lst:
        if lst == lst[::-1]:
            print("palindrome")
        else:
            print("not palindrome")

ceck_palind(lst)


text = "hello world"
text = text.replace(' ', '')  # remove spaces
print(text)

unique_chars = set()  # stores only unique characters

for char in text:
    unique_chars.add(char)

print(unique_chars) # number of unique characters


def is_anagram(s1, s2):

    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("aabb", "abab"))      # True


line = "John,25,Developer"
parts = line.split(",")
print(parts)
name, age, job = parts
print(f"{name} is a {job} aged {age}")
# Output: John is a Developer aged 25
"""
sentence = "hello world"
reversed_words = ' '.join(word[::-1] for word in sentence.split())
print(reversed_words)  # 'olleh dlrow'

