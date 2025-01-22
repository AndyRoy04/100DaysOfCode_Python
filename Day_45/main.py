from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name='a', class_="storylink")
article_scores = soup.select(selector='span .score')
article_links = []
highest_score = 0

for article in articles:
    text = article.get_text()
    link = article['href']
    article_links.append({
        'title': text,
        'link': link,
        'score': 0
    })
for i in range(len(articles)):
    score_board = {}
    score_board['score'] = int(article_scores[i].get_text().split()[0])  #Split the text into a list of 2 and return the first part as an integer
    article_links[i].update(score_board)

for article in article_links:
    if article['score'] > highest_score:
        highest_score = article['score']
        highest_score_article = article
print(f"{highest_score_article['title']}\n{highest_score_article['link']}")
    



























































# with open("100DaysOfCode_Python/Day_45/website.html") as website:
#     content = website.read()
#     # print(content)
    
# soup = BeautifulSoup(content, "html.parser")
# anchors = soup.find_all("a")
# # print(soup.find(name="a", href="https://angelabauer.github.io/cv/hobbies.html"))
# # print(anchors)
# print(soup.select_one(selector="strong a"))

# # for tags in anchors:
# #     print(tags.getText())