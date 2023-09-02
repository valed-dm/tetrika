"""Checks if string consists of latin chars"""

import string


def is_latin(s):
    """Tests if char is latin"""

    char_set = string.ascii_letters
    return all((True if x in char_set else False for x in s))
