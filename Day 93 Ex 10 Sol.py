import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-09-30&sortBy=publishedAt&apiKey=00dd914f2fbb4d2791d1e49b4eb394fe"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")
