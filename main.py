from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

top_movies_tags = soup.find_all(name="h3", class_="title")
top_movies_list = [movie.getText() for movie in top_movies_tags]
top_movies_list.reverse()

text_file = open("top_100_movies.txt", "w")
for element in top_movies_list:
    text_file.write(element + "\n")
text_file.close()




