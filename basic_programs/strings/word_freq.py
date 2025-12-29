text = "selenium python selenium java python python"
frequency = {}

words = text.split()
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)