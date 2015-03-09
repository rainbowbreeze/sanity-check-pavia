__author__ = 'rainbowbreeze'

import dateutil.parser


class Bando:
    """Simple object for storing bando information

    """

    def __init__(self, title, date, url):
        # TODO lowercase the title
        self.title = title
        self.date = date
        self.url = url

    @staticmethod
    def from_json(dictionary):
        return Bando(
            dictionary['title'],
            dateutil.parser.parse(dictionary['date']),
            dictionary['url'])

    def to_json(self):
        return {
            'title': self.title,
            'url': self.url,
            'date': self.date.isoformat()}
        # dict = {}
        # dict['title'] = self.title
        # return dict
        # or
        # return self.__dict__

