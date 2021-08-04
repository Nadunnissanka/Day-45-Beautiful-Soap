from bs4 import BeautifulSoup
import requests

WEBSITE_URL = "https://news.ycombinator.com/news"

response = requests.get(url=WEBSITE_URL)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tags = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
article_upvote_scores = []
for article_tag in article_tags:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)
article_upvotes = soup.find_all(name="span", class_="score")
for article_upvote in article_upvotes:
    article_upvote_score = int(article_upvote.getText().split(" ")[0])
    article_upvote_scores.append(article_upvote_score)

# print(article_texts)
# print(article_links)
# print(article_upvote_scores)

# Find the most up voted article
most_up_votes = max(article_upvote_scores)
most_up_voted_index = int(article_upvote_scores.index(most_up_votes))
print(f"Article: {article_texts[most_up_voted_index]}, Link: {article_links[most_up_voted_index]} got most up votes score. (Score: {article_upvote_scores[most_up_voted_index]})")

