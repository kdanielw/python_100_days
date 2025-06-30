import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
reponse = requests.get(URL)
soup = BeautifulSoup(reponse.text, "html.parser")

movies = [movie.string for movie in soup.find_all("h3", class_="title")]

with open("movies.txt", mode="w") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")