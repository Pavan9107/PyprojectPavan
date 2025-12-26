def non_repeating_character(s):
    str1 = " "
    count = 0
    for i in s:
        if s.count(i) == 1:
            str1 += i
    return str1

print(non_repeating_character("swiss"))





