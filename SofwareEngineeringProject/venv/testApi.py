import json,requests,flask

search_word = "hyde"
response = requests.get("http://gutendex.com/books/?search=" + search_word)
data = json.loads(response.content)
print(data)
