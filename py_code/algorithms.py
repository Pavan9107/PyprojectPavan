"""
s = 'banana'
if 'ana' in s:
    print( 'string found')


text = "I love Python programming"
pattern = "Python"

def find_word_in_text(text, pattern):
    words = text.split()

    for i in range(len(words)):
        if words[i] == pattern:
            return i
    return -1

print(find_word_in_text(text, pattern))  # Output: 2

s = "Race Car"
words = s.lower().split()      # ['race', 'car']
d = ''.join(words)             # 'racecar'
print(d)


words = ['Python', 'is', 'awesome']
sentence = ''.join(words)
print(sentence)  # Python is awesome



from dataclasses import replace

chars = [' ', ' ', 'T', 'h', 'i', 's', ' ', ' ', 'i', 's', ' ', ' ', ' ', 'f', 'u', 'n', ' ', ' ']
d = ''.join(chars).split()
e = ' '.join(d)
print(e)


chars = ['H', 'e', 'l', 'l', 'o', ' ', ',', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '!', ' ', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', '?']
d= ''.join(chars).split()
e = ' '.join(d)
print(e)


text = "This is a beautiful day!"
vowels = 'aeiouAEIOU'
result = ''

for i in text:
    if i not in vowels:
        result += i


print(result,count)

def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    result = ''

    for i in sentence:
        if i in vowels:
            count += 1
        else:
            result += i
    return result,count

print(count_vowels("This is a beautiful day!"))

"""
