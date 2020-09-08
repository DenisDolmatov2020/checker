import pytest

from tests.base import BaseUnitTest
import requests


class TestSearchFilters(BaseUnitTest):
    """
    """
    TEST_API_HOST = ""
    TEST_API_PORT = ""
    TEST_API_VERSION = ""

    payload = dict(building_floors_max=44, building_floors_min=12, floor_max=36, floor_min=4,
                   metro=[62, 85, 14, 48, 70, 28, 13, 63], price_per_m_max=107681600, price_per_m_min=958400,
                   rooms_count=3, total_area_max=260, total_area_min=42, limit=1, building_type=3)

    r = requests.request(method='get', url=TEST_API_HOST, params=payload)

    def test_apartments_search_total_area(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'total_area':
                    assert each.value < self.payload['total_area_max']
                    assert each.value > self.payload['total_area_min']

    def test_apartments_search_price_per_m_min(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'price':
                    assert each.value > self.payload['price_per_m_min']

    def test_apartments_search_price_per_m_max(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'price':
                    assert each.value < self.payload['price_per_m_max']

    def test_apartments_search_floor_per_m_max(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'floor':
                    assert each.value < self.payload['floor_max']

    def test_apartments_search_floor_per_m_min(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'floor':
                    assert each.value < self.payload['floor_min']

    def test_apartments_search_metro_station(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'metro_station':
                    for other in each:
                        if other == 'id':
                            assert other.value == self.payload['metro']

    def test_apartments_search_room_count(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'room_count':
                    assert each.value == self.payload['rooms_count']

    def test_apartments_search_building_floors_min(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'building_floors':
                    assert each.value > self.payload['building_floors_min']

    def test_apartments_search_building_floors_max(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'building_floors':
                    assert each.value < self.payload['building_floors_max']

    def test_apartments_search_building_type(self):
        """

        :return:
        """
        req_url = ''
        k = requests.request("get", req_url, params=self.payload)

        if len(k.content) > 0:

            for each in self.r:
                if each == 'building_type':
                    for other in each:
                        if other == 'id':
                            assert other.value == self.payload['building_type']

    def _test_apartments_search_elevators_type(self):  # !!!!!!!!!!!
        """

        :return:
        """
        self.base_check_request("get", '?elevators_type=2')

    def _test_apartments_search_ipoteka(self):
        """

        :return:
        """
        self.base_check_request("get", '?credit=mortgage&limit=12')

    def _test_apartments_search_living_area(self):
        """

        :return:
        """
        self.base_check_request("get", '?living_area_min=28&living_area_max=131')

    def _test_apartments_search_regions(self):
        """

        :return:
        """
        self.base_check_request("get", '?name=%D0%BA')
