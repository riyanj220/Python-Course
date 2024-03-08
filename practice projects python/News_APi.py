import requests
import json

query = input("what type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-09-10&sortBy=publishedAt&apiKey=40b6f45830654538b7a98c2fc18a5b66"
r = requests.get(url)
news = json.loads(r.text)
# print(new, type(new))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------")
