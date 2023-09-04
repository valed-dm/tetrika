"""Parses main table from wiki page as simple example"""

import io

import pandas as pd
import requests

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
# cats = [">А<", ">Б<", ">В<", ">Г<", ">Д<", ">Е<", ">Ж<", ">З<"]


if __name__ == "__main__":
    r = requests.get(url, timeout=10)
    website = io.StringIO(r.text)
    # for string in website:
    #     if 'table role="presentation"' in string:
    #         spl = string.split(" ")
    #         filtered = filter(lambda x: x.startswith("href="), spl)
    #         print(list(filtered))
    #     if any(substring in string for substring in cats):
    #         print(string, "\n")
    tables_on_page = pd.read_html(website, encoding="utf-8")
    table = tables_on_page[0]
    table.to_csv("outputs/presentation.csv", index=False, encoding="utf-8")
