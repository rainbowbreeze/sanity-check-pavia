
__author__ = 'rainbowbreeze'

import os
from logic.contentdownloader import ContentDownloader
from logic.scraper import Scraper
from logic.itemsmanager import ItemsManager

def dostuff():
    with open('mainfile.py', 'r') as f:
        read_line = f.read()
        print(read_line)
    f.closed

if __name__ == "__main__":
    print "ciao"
    # dostuff()

    # Downloads the page
    downloader = ContentDownloader()
    page = downloader.downloadPage("http://www.sanmatteo.org/site/home/il-san-matteo/albo-on-line.html")

    if not page:
        print("Cannot download the page :(")

    else:
        # Parses it
        scraper = Scraper()
        items_scraped = scraper.parsePage(page)

        items_manager = ItemsManager()
        for bando in items_scraped:
            base, ext = os.path.splitext(bando.url)
            print base, ext
            items_manager.downloadBando(bando)