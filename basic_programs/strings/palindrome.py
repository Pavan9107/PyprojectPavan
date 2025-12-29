text = "madam"
reverse_text = ""
for char in text:
    reverse_text = char + reverse_text

print(reverse_text)

if reverse_text == text:
    print("palindrome")


