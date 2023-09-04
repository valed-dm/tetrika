"""Checks if string consists of latin chars"""

import string


def is_latin(s):
    """Tests if char is latin"""

    char_set = string.ascii_letters
    return all((x in char_set for x in s))
