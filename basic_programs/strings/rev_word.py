text = "i love automation"
# output → "automation love i"
word = ""
list_words = []
for i in text:
    if i != " ":
        word += i

    else:
        list_words.append(word)
        word = ""

list_words.append(word)

print(list_words)

rev_list = []
for word in range(len(list_words)-1,-1,-1):
    rev_list.append(list_words[word])

print(rev_list)

result = ""
for w in rev_list:
    result += w + " "

print(result.strip())
