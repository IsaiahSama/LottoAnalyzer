"""This file will be responsible for beautifying the HTML and returning the page withut the barrier"""

from bs4 import BeautifulSoup

def make_soup(html: str):
    soup = BeautifulSoup(html, features="html.parser")
    return soup

def remove_wall(html: str) -> str:
    soup = make_soup(html, features="html.parser")

    ageContainer = soup.find(id="ageContainer")
    if ageContainer:
        ageContainer.extract()
    return soup.prettify()