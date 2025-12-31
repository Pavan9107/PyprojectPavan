def process_sentence(text):
    word = ""
    result = ""

    for char in text:
        if char != " ":
            word += char
        else:
            if word != "":
                for i in range(len(word)-1, -1, -1):
                    result += word[i]
                result += " "
                word = ""

    # handle last word
    if word != "":
        for i in range(len(word)-1, -1, -1):
            result += word[i]

    return result.strip()



print(process_sentence("  i   love   automation  "))


