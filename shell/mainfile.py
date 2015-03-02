__author__ = 'rainbowbreeze'

from logic.contentdownloader import ContentDownloader

def dostuff():
    with open('mainfile.py', 'r') as f:
        read_line = f.read()
        print(read_line)
    f.closed

if __name__ == "__main__":
    print "ciao"
    # dostuff()
    downloader = ContentDownloader()
    page = downloader.downloadPage("http://www.sanmatteo.org/site/home/il-san-matteo/albo-on-line.html")
    print(page)