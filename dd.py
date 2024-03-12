"""This file will be responsible for dealing with the Double Draw website."""

from requests import get, post
from beautifier import remove_wall, make_soup

URL = "https://www.mybarbadoslottery.com/games/double-draw"

HISTORY_URL = "https://www.mybarbadoslottery.com/check-history/double-draw"

data = {
    "date": "01/01/2024"
}

# response = post(HISTORY_URL, data=data)
# response.raise_for_status()

# text = response.text

# with open("test.html", "w") as fp:
#     fp.write(remove_wall(text))

def parse_test():
    with open("test.html") as fp:
        data = fp.read()
    
    panel_results = []

    soup = make_soup(data)

    # result_divs = soup.find_all(_class="draw-results", name="div")

    selector = "#content > div.container > div > div.content-panel > div:nth-child(4) > div > ul > li:nth-child({0}) > div.panel-result > div > div > div > ul:nth-child(2)"

    for i in range(1, 5):
        container = soup.select(selector.format(i))
        panel_results.append(container)

    pr = panel_results[0][0]
    list_items = pr.find_all("li")[1:]

    print([int(li.text.strip()) for li in list_items])

if __name__ == "__main__":
    parse_test()

