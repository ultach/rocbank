import requests
from bs4 import BeautifulSoup
from decimal import Decimal

URL = "http://www.cbr.ru/scripts/XML_daily.asp"


def get_rates():
    rev = requests.get(URL)
    soup = BeautifulSoup(rev.content, "xml")

    rates = {
        i.CharCode.string: (
            Decimal(i.Value.string.replace(",", ".")),
            int(i.Nominal.string),
        )
        for i in soup("Valute")
    }

    return rates


def _main():
    rates = get_rates()

    result = (rates["AUD"][0] / rates["AUD"][1]) / (rates["BYN"][0] / rates["BYN"][1])
    print({"cbr_course": float(result.quantize(Decimal(".01")))})


if __name__ == "__main__":
    _main()
