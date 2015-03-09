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

    def buildPathName(self, baseDir, fileName):
        """From a directory and a file, build the final path

        :param baseDir:
        :param fileName:
        :return:
        """
        pass

    def find_new_item_to_download(self, items_scraped):
        """Search for the item that need to be dowloaded

        :param items_scraped:
        :return:
        """
        # Reads the items already downloaded
        items_downloaded = self._read_saved_items_from_file(self._controlFileName)
        # Compares with the new items
        new_items = self._search_for_new_items(items_downloaded, items_scraped)
        return new_items

    def save_to_control_file(self, new_items_downloaded):
        """Saved the list of element downloaded

        :param new_items_downloaded:
        :return:
        """

        if not new_items_downloaded or 0 == len(new_items_downloaded):
            print "Nothing to add to the file, exiting"
            return

        items_total = self._read_saved_items_from_file(self._controlFileName)
        items_total.extend(new_items_downloaded)

        # Unicode support
        # http://stackoverflow.com/questions/12309269/write-json-data-to-file-in-python
        with io.open(self._controlFileName, "a", encoding='utf-8') as outfile:
            outfile.write(unicode(
                json.dumps(
                    items_total,
                    outfile,
                    indent=2,
                    default=self._to_json,
                    ensure_ascii=False)
            ))

    def _search_for_new_items(self, items_downloaded, items_scraped):
        """From all the scraped items, returns only the ones that that need to
        be downloaded because are new

        :param items_downloaded: items already downloaded
        :param items_scraped: items scraped
        :return: a list of items that need to be downloaded
        """
        # Pythonic way to return the items that are not present in the saved list
        new_items = [x for x in items_scraped if x not in items_downloaded]
        return new_items

    def _to_json(self, obj):
        if isinstance(obj, Bando):
            return obj.to_json()
        #if isinstance(obj, datetime):
        #    serial = obj.isoformat()
        #    return serial
        return obj.__dict__

    def _read_saved_items_from_file(self, file_name):
        """
        Reads already downloaded items from a file and put them in a list

        :return: a list of Bando objects
        """
        # http://stackoverflow.com/questions/82831/check-if-a-file-exists-using-python
        if not os.path.isfile(file_name):
            print "Control file doesn't exist"
            return []

        # Loads already saved bando items
        with open(file_name, "r") as source_data:
            saved_items_json = json.load(
                source_data)

        # Transforms it in a list of objects
        saved_items = []
        for obj in saved_items_json:
            saved_items.append(Bando.from_json(obj))
        return saved_items


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

