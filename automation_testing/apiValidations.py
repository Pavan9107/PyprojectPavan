import requests

URL = "http://216.10.245.166/Library/Addbook.php"
book_data = {
"name":"Learn API",
"isbn":"bcad",
"aisle": "2267",
"author": "Pavansss"
}

result = requests.post(url=URL, json=book_data)

print(result.text)
print(type(result.text))

Url= "http://216.10.245.166/Library/GetBook.php?AuthorName=pavan"
result = requests.get(url=Url)
print(result.text)
print(type(result.text))




