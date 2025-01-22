import requests
from bs4 import BeautifulSoup

URL = 'https://www.reddit.com/r/anime/comments/y95zjn/top_100_most_acclaimed_anime_series_of_all_time/?rdt=58665'

response = requests.get(URL)
anime_website = response.text

# Extracting the names and links of the top 100 most acclaimed anime series
soup = BeautifulSoup(anime_website, 'html.parser')
anime_list = soup.find_all(name='a', rel='noopener nofollow ugc')
index = 0

with open('100DaysOfCode_Python/Day_45/Animes Scrape/Animes_to_watch.txt', 'w', encoding='utf-8') as anime_file:
    for anime in anime_list[5:]:
        index += 1
        anime_title = anime.getText()
        anime_link = anime['href']
        anime_file.write(f"{index}) {anime_title} :\n\t\t\t\t{anime_link}\n")
