import io

__author__ = 'rainbowbreeze'

import glob
import json
import os.path
from datetime import datetime
from domain.bando import Bando

class ItemsManager:
    """Manages item, compares them with the existing ones and, in case, download new ones

    """

    def __init__(self):
        self._downloadDir = "downloaded"
        self._controlFileName = "items_downloaded.txt"


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

    def checkForNewItems(self, items_scraped):
        """

        :param items_scraped:
        :return:
        """

        # http://stackoverflow.com/questions/82831/check-if-a-file-exists-using-python
        if not os.path.isfile(self._controlFileName):
            print "Control file doesn't exist"
            return items_scraped

        # Loads already saved bando items
        with open(self._controlFileName, "r") as source_data:
            saved_items_json = json.load(source_data)

        # Transforms it in list of objects
        saved_items = []
        for obj in saved_items_json:
            saved_items.append(Bando.from_json(obj))

        # Returns the items that are not present in the saves list
        new_items = [x for x in items_scraped if x not in saved_items]
        return new_items

    def _to_json(self, obj):

        if isinstance(obj, Bando):
            return obj.to_json()
        #if isinstance(obj, datetime):
        #    serial = obj.isoformat()
        #    return serial
        return obj.__dict__

    def saveToControlFile(self, items_scraped):
        """

        :param items_scraped:
        :return:
        """

        # Unicode support
        # http://stackoverflow.com/questions/12309269/write-json-data-to-file-in-python
        with io.open(self._controlFileName, "a", encoding='utf-8') as outfile:
            outfile.write(unicode(
                json.dumps(
                    items_scraped,
                    outfile,
                    indent=2,
                    default=self._to_json,
                    ensure_ascii=False)
            ))

"""
        json_dict = json.loads(data)

        for obj in json_dict:
            print(obj)
            print(Bando.from_json(obj).date)
            print("------------")


import io, json
with io.open('data.txt', 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(data, ensure_ascii=False)))
        """

