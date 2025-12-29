s = "automation"
s1 = list("automation")
vowels = "aeiouAEIOU"
left =0
right = len(s1)-1
result = ""
while left < right:
    if s1[left] not in vowels:
        left += 1
    elif s1[right] not in vowels:
        right -=1
    else:
        s1[left],s1[right] = s1[right],s1[left]
        left +=1
        right -=1
result = ''.join(s1)
print(result)
