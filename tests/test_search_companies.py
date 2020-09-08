import pytest
import requests

from tests.base import BaseUnitTest


class TestSearchComplexes(BaseUnitTest):

    TEST_API_HOST = ''
    # "?search=a&limit=1&offset=0&type=2"

    payload = dict(search=1, limit=1, offset=0, type=2)

    r = requests.request(method='get', url=TEST_API_HOST, params=payload)

    def test_companies_type(self):
        """

        :return:
        """
        # req_url = 'http://api.test-ogd.ru/v1.0/count/companies/'
        # k = requests.request("get", req_url, params=self.payload)
        #
        # if len(k.content) > 0:
        res = 0
        for each in self.r:
            if each == 'type':
                res = 1
                assert each.value == self.payload['type'] & res == 1


    def test_companies_name(self):
        """

        :return:
        """
        # req_url = ''
        # k = requests.request("get", req_url, params=self.payload)

        # if len(k.content) > 0:
        self.res = 0
        for each in self.r:
            if each == 'search':
                self.res = 1
                assert self.payload['search'] in each.value