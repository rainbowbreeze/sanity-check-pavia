__author__ = 'rainbowbreeze'

import os
import glob
from datetime import datetime

class ItemsManager:
    """Manages item, compares them with the existing ones and, in case, download new ones

    """

    def __init__(self):
        self._downloadDir = "downloaded"


    def downloadBando(self, bando):
        file_name = "{0}-{1}".format(datetime.strftime(bando.date, "%Y%m%d"), "aaa")
        print(file_name)

    def checkForDuplicates(self, all_file_urls):
        """From a list of item to download, returns only the ones to download,
           cutting off the ones already present in the download directory;

        :param all_file_urls:
        :return:
        """
        files_downloaded = glob.glob()
        for file in files_downloaded:
            print(file)


    def generateChecksumFromUrl(self, url):
        """From a resource url, generate a checksum that correspond to the name of the file

        :param url:
        :return:
        """
        pass

    def buildPathName(self, baseDir, fileName):
        """From a directory and a file, build the final path

        :param baseDir:
        :param fileName:
        :return:
        """
        pass
