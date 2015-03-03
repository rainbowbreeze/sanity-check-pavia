__author__ = 'rainbowbreeze'

from logic.contentdownloader import ContentDownloader
from logic.scraper import Scraper

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

    # Parses it
    scraper = Scraper()
    result = scraper.parsePage(page)
    print(result)