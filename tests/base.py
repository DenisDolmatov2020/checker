import json
import os
import unittest

import requests

import json


class BaseUnitTest(unittest.TestCase):
    """
    Base test class with common init functions
    """
    TEST_API_HOST = ""
    TEST_API_PORT = ""
    TEST_API_VERSION = "v1.0"

    @classmethod
    def setUpClass(cls):
        """
        """
        cls.TEST_API_HOST = os.environ.get("TEST_API_HOST", cls.TEST_API_HOST)
        cls.TEST_API_PORT = os.environ.get("TEST_API_PORT", cls.TEST_API_PORT)
        cls.TEST_API_VERSION = os.environ.get("TEST_API_VERSION", cls.TEST_API_VERSION)
        api_host = cls.TEST_API_HOST
        if cls.TEST_API_PORT:
            api_host = "{}:{}/".format(api_host.rstrip("/"), cls.TEST_API_PORT)

        cls.TEST_API_URL = "/".join([x.strip("/") for x in [api_host, cls.TEST_API_VERSION] if x])

    @classmethod
    def tearDownClass(cls):
        """
        """

    def build_url(self, url):
        """
        Build full url
        """
        return "/".join(x.lstrip("/") for x in (self.TEST_API_URL, url))

    def make_req(self, method, url, json=None, **kwargs):
        """
        Process request to url
        """
        req_url = self.build_url(url)
        r = requests.request(method, req_url, json=json, **kwargs)

        return r

    def base_check_request(self, method, url, **kwargs):
        """
        Filter request by default checks.
        status 200, non-empty answer
        valid json response
        """
        r = self.make_req(method, url, **kwargs)

        req_url = r.request
        self.assertEqual(r.status_code, 200, "Invalid response code: {}".format(req_url.url))
        self.assertGreater(len(r.content), 0, "Empty response body: {}".format(req_url.url))

        try:
            j = r.json()
        except json.decoder.JSONDecodeError:
            j = None

        self.assertIsNotNone(j, "Json decode error: {}".format(req_url))

        return j

    def check_request_keys(self, method, url, keys, **kwargs):
        """
        Check dict request keys 
        """
        r = self.base_check_request(method, url, **kwargs)
        self.assertIsInstance(r, dict)
        self.assertListEqual(sorted(list(r.keys())), keys)

        return r

    def check_list_item_keys(self, elm_list, keys, allow_empty=False):
        """
        Check keys of one list item element
        """
        self.assertIsInstance(elm_list, list)
        if allow_empty and len(elm_list) == 0:
            return

        keys = sorted(keys)
        for elm in elm_list:
            self.assertListEqual(sorted(list(elm.keys())), keys)

    def check_list_items_type(self, elm_list, elm_type):
        """
        Check type of list elements
        """
        self.assertIsInstance(elm_list, list)
        for v in elm_list:
            self.assertIsInstance(v, elm_type)

    def check_r_values(self, method, url, **kwargs):
        """
        Return dict with values of request
        """
        r = self.make_req(method, url, **kwargs)
        return r.json
