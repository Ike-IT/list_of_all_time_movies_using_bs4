import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_webpage = response.text
# print(empire_webpage)

soup = BeautifulSoup(empire_webpage, "html.parser")
# print(soup)
movie_list = [(movie.getText()) for movie in soup.find_all(name="h3", class_="title")]
movies = movie_list[::-1]
# print(movies)
with open("movies.txt", mode="w", errors="ignore") as file:
    for movie in movies:
        # print(movie)
        file.write(f"{movie}\n")

