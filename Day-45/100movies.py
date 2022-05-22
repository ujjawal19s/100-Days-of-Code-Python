import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

with open("movies.txt", mode="w") as file:
    names_list = [name.getText().split(' ', 1)[1] for name in soup.find_all(name="h3", class_="title")]
    names_list.reverse()
    num = 1
    for name in names_list:
        file.write(f"{num}) {name}\n")
        num += 1



