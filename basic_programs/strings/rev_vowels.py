s = "This is to check vowels rev"
chars = list(s)

left = 0
right = len(chars)-1
vowels = "aeiouAEIOU"


while left < right:
    if chars[left] not in vowels:
        left += 1

    elif chars[right] not in vowels:
        right -= 1

    else:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

final =''.join(chars)


print(s)
print(chars)
print(final)

