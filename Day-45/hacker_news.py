from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

article_links = [article_tag.get("href") for article_tag in articles]

article_upvote = [int(soup.getText().split()[0]) for soup in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_texts)
# print(article_links)
# print(article_upvote)
