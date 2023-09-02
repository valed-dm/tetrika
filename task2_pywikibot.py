"""Creates outputs/beasts.csv"""

from utils import cat_counter, get_beast_csv, get_wiki_pages, is_latin, ru_latin_total


def main():
    """Creates beasts.csv"""

    ru_beasts = {}
    lat_beasts = {}
    for cat in get_wiki_pages("ru", "Животные_по_алфавиту"):
        key = cat.title()[0]
        if is_latin(key):
            cat_counter(key, lat_beasts)
        elif not is_latin(key):
            cat_counter(key, ru_beasts)

    ru_latin_total({**ru_beasts, **lat_beasts})
    get_beast_csv(ru_beasts, lat_beasts)


if __name__ == "__main__":
    main()
