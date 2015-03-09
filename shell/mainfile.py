import json

__author__ = 'rainbowbreeze'

import os
from logic.contentdownloader import ContentDownloader
from logic.scraper import Scraper
from logic.itemsmanager import ItemsManager

def dostuff():
    with open('mainfile.py', 'r') as f:
        read_line = f.read()
        print(read_line)

# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
def main():
    print "ciao"
    # dostuff()

    # Downloads the page
    downloader = ContentDownloader()
    page = downloader.downloadPage("http://www.sanmatteo.org/site/home/il-san-matteo/albo-on-line.html")

    if not page:
        print("Cannot download the page :(")
        return

    # Parses it
    scraper = Scraper()
    items_scraped = scraper.parsePage(page)

    items_manager = ItemsManager()

    # Downloads only new items
    new_items = items_manager.checkForNewItems(items_scraped)
    for bando in new_items:
        print(bando.__dict__)
        #print(json.dumps(bando))
        #base, ext = os.path.splitext(bando.url)
        #print base, ext
        #items_manager.downloadBando(bando)

    # Finally, saves the new items to the control file
    #items_manager.saveToControlFile(items_scraped)

    return

if __name__ == "__main__":
    main()