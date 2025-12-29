text = "I love python"
word = " "
final = []
for i in text:
    if i!= " ":
        word += i
    else:
        temp = ""
        for ch  in word:
            temp = ch + temp
        final.append(temp)
        word = " "

rev = ""
for ch in word:
    rev = ch +rev

final.append(rev)
print(final)

