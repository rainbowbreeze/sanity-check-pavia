import json

__author__ = 'rainbowbreeze'

import unittest
import datetime
from domain.bando import Bando


class TestBando(unittest.TestCase):
    def test_equality(self):
        now = datetime.datetime.now()
        bando1 = Bando("Title1", now, "http://urlfile1.zip")
        bando2 = Bando("Title1", now, "http://urlfile1.zip")
        bando3 = Bando("Title2", now, "http://urlfile1.zip")
        now2 = datetime.datetime.now()
        bando4 = Bando("Title2", now2, "http://urlfile1.zip")
        bando5 = Bando("Title2", now2, "http://urlfile2.zip")

        self.assertEqual(bando1, bando2)
        self.assertNotEqual(bando1, bando3)
        self.assertNotEqual(bando2, bando3)
        self.assertNotEqual(bando3, bando4)
        self.assertNotEqual(bando4, bando5)
        self.assertEqual(len(set([bando1, bando2])), 1)
        self.assertEqual(len(set([bando1, bando3])), 2)
        self.assertEqual(len(set([bando2, bando3])), 2)
        self.assertEqual(len(set([bando1, bando2, bando3])), 2)
        self.assertEqual(len(set([bando1, bando2, bando3, bando4, bando5])), 4)

    def test_json(self):
        now = datetime.datetime.now()
        bando1 = Bando("Title1", now, "http://urlfile1.zip")
        json_dict = bando1.to_json()
        self.assertTrue(json_dict)
        bando2 = Bando.from_json(json_dict)
        self.assertEquals(bando1, bando2)


if __name__ == '__main__':
    unittest.main()
