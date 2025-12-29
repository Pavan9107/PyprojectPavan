
"""
print(type(str))

res = str[::-1]
print(res)

rese = ''.join(reversed(str))
print(rese)

reverse_str = " "
for i in range(len(str)-1,-1,-1):
    reverse_str  += str[i]

print(reverse_str)

s = "abcabc"

a = list(s)
a.reverse()
print(a)
b = ''.join(a)
print(b)



s = "Hello"
def reverse_alpha(s):
    if len(s)== 0:
        return s

    return reverse_alpha(s[1:])+s[0]
print(reverse_alpha(s))


#Palindrome
Pal_s = "MadaM"
rev_s = Pal_s[::-1]
print(rev_s)
if (rev_s == Pal_s):
    print("palindrome")
else:
    print("not palindrome")


s = "level"
s = s.lower()
rev = s[::-1]
if s == rev:
    print("palindrome")
else:
    print("not palindrome")


s = "Nurses run"
s = s.lower()
s = s.replace(" ","")
print(s)

r = s[::-1]
print(r)
if (s == r):
    print("palindrome")
else:
    print("not palindrome")



s = "A man, a plan, a canal: Panama"
s = s.lower()

cleaned = "".join(c for c in s if c.isalnum())
print(cleaned)

rev = cleaned[::-1]
print(rev)

if (cleaned == rev):
    print("palindrome")
else:
    print("not palindrome")


def check_palindromes():
    strings = ["python", " python is awesome", "basics", "Madam", "nurses run"]

    for s in strings:
        cleaned = s.lower().replace(" ", "")
        print(cleaned)
        if cleaned == cleaned[::-1]:
            print(f"'{s}' → Palindrome ✅")
        else:
            print(f"'{s}' → Not a palindrome ❌")

check_palindromes()

reversed("hello")
a = list(reversed("hello"))
b = ''.join(a)
print(b)

b, c, d = 1, 2, 3
print(b, c, d)
print(f"value is", b)
print("{} {}".format("value is", c))
print("value is" f" {d}")

name = "Alice"
age =30
print(f"{name} is {age} years old")


check_tuple = (1,2,3,4,5)
check_tuple.insert(10)
print(check_tuple)


d = {(1, 2): "check hashability"}
print(d[(1,2)])

"""

def rev_str(s):
    r = ""
    for i in range(len(s)-1,-1,-1):
        r += s[i]
    return r
print(rev_str("hello"))




s= "hello world"
temp = ""
for i in s:
    temp = i + temp

print(temp)

