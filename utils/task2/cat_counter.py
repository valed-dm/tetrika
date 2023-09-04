"""To count beasts in each subcategory"""


def cat_counter(key, dictionary):
    """Dictionary counter"""

    if key in dictionary.keys():
        dictionary[key] += 1
    else:
        dictionary[key] = 1
