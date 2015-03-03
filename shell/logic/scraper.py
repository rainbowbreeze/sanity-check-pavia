__author__ = 'rainbowbreeze'

import bs4
from domain.bando import Bando
from datetime import datetime

class Scraper:
    """Parses a downloaded page and find items to download

    Some info on:
      http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python
      http://jakeaustwick.me/python-web-scraping-resource/
    """

    def __init__(self):
        self._base_url = "http://www.sanmatteo.org"
        pass

    def parsePage(self, page):
        """
        Parses a page ad identifies items to download
        :param page: the content of the page to download
        :return: the list if items to download, url by url
        """
        print("Parsing the page...")
        soup = bs4.BeautifulSoup(page)
        # links = soup.select('div.bando a[href^=/video]')
        links = []
        # for h2 in soup.select('article.bando h2'):
        for bando_full in soup.select("article.bando"):
            title = bando_full.h2.string

            # Examines all the rows in the page block
            url = ""
            date = ""
            for row in bando_full.select("div.row"):
                # Searches for particular labels
                label = row.select("div.label")
                if len(label) > 0 and label[0].string:
                    label_lower = label[0].string.lower()
                    if "allegato" == label_lower:
                        url = self._base_url + row.a.get("href")
                    if "data provvedimento" == label_lower:
                        value = row.select("div.value")
                        date = datetime.strptime(value[0].string, "%d/%m/%Y") # 18/02/2015

            # Checks for the extrapolated data
            if title and url and date:
                bando_data = Bando(title, date, url)
                links.append(bando_data)
            else:
                print("Cannot save data for " + title)

        return links