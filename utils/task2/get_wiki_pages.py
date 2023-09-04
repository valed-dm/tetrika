"""Wiki beast's pages generator"""

import pywikibot


def get_wiki_pages(code, title):
    """Creates pywikibot pages generator"""

    site = pywikibot.Site(code, "wikipedia")
    category = pywikibot.Category(site, title)
    print(category.categoryinfo)
    page_gen = category.articles()
    return page_gen
