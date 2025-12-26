s = "This is to check vowels rev"
chars = list(s)

left = 0
right = len(chars)-1
vowels = "aeiouAEIOU"

while left < right:
    if not chars[left].isalpha() or chars[left] in vowels:
        left +=1

    elif not chars[right].isalpha()  or chars[right] in vowels:
        right -=1

    else:
        chars[left],chars[right] = chars[right],chars[left]
        left +=1
        right -=1

result = "".join(chars)

print(result)