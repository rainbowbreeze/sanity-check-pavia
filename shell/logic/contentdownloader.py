__author__ = 'rainbowbreeze'

import requests

class ContentDownloader:
    """Downloads pages from the Internet

    """

    def __init__(self):
        pass

    def downloadPage(self, page_url):
        """Downloads a page from the Internet

        :param page_url: url of the page to download
        :return: a string object that contains the downloaded page
        """
        print("Downloading page at " + page_url)
        response = requests.get(page_url)
        return response.text


    def downloadFile(self, fileUrl, fileName):
        """Download a given files from the Internet and save it on a given file

        :param fileUrl:
        :param fileName:
        :return:
        """
        pass