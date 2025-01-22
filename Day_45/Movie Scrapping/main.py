import requests
from bs4 import BeautifulSoup
from pprint import pprint


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_archieve_page = response.text

soup = BeautifulSoup(web_archieve_page, 'html.parser')
movies_list = soup.find_all(name='h3', class_='title')
order_list = list(reversed(movies_list))

with open('100DaysOfCode_Python/Day_45/Movie Scrapping/to_watch.txt', 'w', encoding='utf-8') as movie_file:
    for movie in order_list:
        movie_name = movie.getText()
        movie_file.write(f'{movie_name}\n')
        