# def str_word(s):
#     words = s.split()
#     words.reverse()
#     return ''.join(words)
# print(str_word("hello world"))


def str_rev_word(s):

#converting string into list
    current_word = ""
    list_words = []
    for letter in s:
        if letter == " ":
            list_words.append(current_word)
            current_word = ""
        else:
            current_word += letter

    list_words.append(current_word)

#pointer window to swap the elements in list
    left = 0
    right = len(list_words) - 1
    while left < right:
        list_words[left],list_words[right] = list_words[right],list_words[left]
        left += 1
        right -= 1

    print(list_words)

#covert back the reversed list to string
    final_rev_str = ""
    for i in range(len(list_words)):
        final_rev_str += list_words[i]
        if i!= len(list_words) - 1:
            final_rev_str += " "
    return final_rev_str

print(str_rev_word("hello world"))






