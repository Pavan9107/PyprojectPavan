s = "a1b2c3d4"
char = list(s)

left = 0
right = len(char) - 1
digit_check = "0123456789"

while left < right:
    if char[left] not in digit_check:
        left += 1

    elif char[right] not in digit_check:
        right -= 1

    else:
        char[left], char[right] = char[right], char[left]
        left += 1
        right -= 1

final_result = "".join(char)

print(final_result)