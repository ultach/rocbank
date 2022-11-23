import re
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/w/index.php"


def get_html(url, **kwards):

    r = requests.get(url, **kwards)
    print(r.url)

    if r.status_code != 200:
        raise requests.ConnectionError(
            "Expected status code 200, but got {}".format(r.status_code)
        )

    return r.text


def extract_total_pages(html):

    soup = BeautifulSoup(html, "lxml")

    tag = soup.find("div", "results-info")
    return tag.attrs.get("data-mw-num-results-total") if tag else None


def _main():

    html = get_html(
        URL, params={"search": "rosbank1"}
    )  # for some queries wiki redirects directly to the article
    total_pages = extract_total_pages(html) or 0

    print({"article_count": total_pages})


if __name__ == "__main__":
    _main()
