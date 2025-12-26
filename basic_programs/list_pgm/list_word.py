names = ["java", "python", "c", "selenium"]

result = []

for i in range(len(names)):
    if len(names[i]) > 4:
        result.append(names[i])

print(result)
