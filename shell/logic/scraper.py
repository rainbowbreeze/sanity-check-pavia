__author__ = 'rainbowbreeze'

import bs4
from domain.bando import Bando

class Scraper:
    """Parses a downloaded page and find items to download

    Some info on:
      http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python
      http://jakeaustwick.me/python-web-scraping-resource/
    """

    def __init__(self):
        pass

    def parsePage(self, page):
        """
        Parses a page ad identifies items to download
        :param page: the content of the page to download
        :return: the list if items to download, url by url
        """
        soup = bs4.BeautifulSoup(page)
        # links = soup.select('div.bando a[href^=/video]')
        links = []
        # for h2 in soup.select('article.bando h2'):
        for bando_full in soup.select('article.bando'):
            title = bando_full.h2.string
            print(title)
            rows = bando_full.find_all('div')
            print rows[-1].a.get('href')
            # rows = h2
            bando_data = Bando(title, '')
            links.append(bando_data)

        return links