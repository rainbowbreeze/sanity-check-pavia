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

    """
    Sources on compairing for equality
     http://jcalderone.livejournal.com/32837.html
     http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    """
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))
