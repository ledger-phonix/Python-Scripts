import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/top-headlines?country=in&category={query}&apiKey=d080d2bf9bac4904abf10948b7512925"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  