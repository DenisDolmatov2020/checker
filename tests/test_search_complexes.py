import pytest
import requests

from tests.base import BaseUnitTest



class TestSearchComplexes(BaseUnitTest):

    """

    """
    TEST_API_HOST = ""
    payload = dict(price_per_m_max=107681600, price_per_m_min=958400, room_count=2, metro=[62, 85, 14, 48, 70, 28, 13, 63], limit=1)

    r = requests.request(method='get', url=TEST_API_HOST, params=payload)

    def test_metro_stations(self):

        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'metro':
                    assert each.value in self.payload['metro']

        else:
            assert False

    def test_price_per_m_max(self):

        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'metro':
                    assert each.value < self.payload['price_per_m_max']
        else:
            assert False

    def test_price_per_m_min(self):
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'metro':
                    assert each.value < self.payload['price_per_m_max']
        else:
            assert False


    def test_rooms_count(self):
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'rooms_count':
                    assert each.value == self.payload['rooms_count']
        else:
            assert False
