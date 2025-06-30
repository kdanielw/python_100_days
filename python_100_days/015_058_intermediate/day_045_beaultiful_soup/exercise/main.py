from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

news_titles = []
news_links = []
news_upvotes = []

for news in soup.find_all("span", class_="titleline"):
    news_titles.append(news.find(name="a").string)
    news_links.append(news.find(name="a").get("href"))
    news_upvotes.append(int(news.find_next("span", class_="score").string.split(" ")[0]))

max_upvotes_index = news_upvotes.index(max(news_upvotes))
print(news_titles[max_upvotes_index])
print(news_links[max_upvotes_index])
print(news_upvotes[max_upvotes_index])