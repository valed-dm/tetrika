"""Creates general parsing result info data"""


from utils.task2 import is_latin


def ru_latin_total(beasts):
    """Wiki parsing general info"""

    total = 0
    latin = 0
    russian = 0

    for k in beasts.keys():
        total += beasts[k]
        if is_latin(k):
            latin += beasts[k]
        else:
            russian += beasts[k]

    print("total beasts:", total, "ru:", russian, "latin:", latin)
