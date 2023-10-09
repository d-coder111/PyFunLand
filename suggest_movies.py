import requests
import random
import sys
from bs4 import BeautifulSoup

session = requests.Session()


def pick_random():
    url = "https://www.imdb.com/chart/top/"
    response = session.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # required tags
    tags = soup.select("td.titleColumn")
    inner_tags = soup.select("td.titleColumn a")
    rating_tag = soup.select("td.ratingColumn")

    # required list
    movies = [tag.text for tag in inner_tags]
    rating = [(rating_tag[i].text.strip("\n"))
              for i in range(0, len(rating_tag), 2)]
    years = [int(tag.span.text.strip("()")) for tag in tags]
    cast_list = [tag["title"] for tag in inner_tags]

    return movies, rating, years, cast_list


def main():

    movies, rating, years, cast_list = pick_random()

    while True:
        rand_index = random.randrange(0, len(movies))

        print(
            f"Title: {movies[rand_index]} | Rating: {rating[rand_index]} | Year: {years[rand_index]} | Cast: {cast_list[rand_index]}")

        cont = input("Want more movies? (Y/N): ")

        if (cont.upper() == "N"):
            sys.exit()


if __name__ == "__main__":
    main()
