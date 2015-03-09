__author__ = 'rainbowbreeze'

import unittest
import datetime
from domain.bando import Bando
from logic.itemsmanager import ItemsManager

class TestItemsManager(unittest.TestCase):

    def test_checkForNewItems(self):
        # Creates the list of download object
        items_manager = ItemsManager()
        items_downloaded = []
        items_new = []
        now = datetime.datetime.now()

        now = datetime.datetime.now()
        bando1 = Bando("Title1", now, "http://urlfile1.zip")
        bando2 = Bando("Title2", now, "http://urlfile1.zip")
        now2 = datetime.datetime.now()
        bando3 = Bando("Title3", now2, "http://urlfile3.zip")
        bando4 = Bando("Title4", now2, "http://urlfile4.zip")
        bando5 = Bando("Title5", now, "http://urlfile5.zip")

        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertFalse(result)

        items_new.append(bando1)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertTrue(result)
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0], bando1)

        items_downloaded.append(bando1)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertFalse(result)

        items_new.append(bando2)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertTrue(result)
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0], bando2)

        items_downloaded.append(bando2)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertFalse(result)

        items_downloaded.append(bando3)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertFalse(result)

        items_new.append(bando4)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertTrue(result)
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0], bando4)

        items_new.append(bando5)
        result = items_manager._search_for_new_items(items_downloaded, items_new)
        self.assertTrue(result)
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0], bando4)
        self.assertEquals(result[1], bando5)


if __name__ == '__main__':
    unittest.main()
