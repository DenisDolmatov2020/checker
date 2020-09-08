from tests.base import BaseUnitTest


class TestUrls(BaseUnitTest):
    """

    """
    TEST_API_HOST = ""
    TEST_API_PORT = ""
    TEST_API_VERSION = ""

    def test_checkerboard_menu_urls(self):
        self.base_check_request("get", "autocomplete/complex/")

    def test_checkerboard_templates_urls(self):
        self.base_check_request("get", "autocomplete/location/")

    def test_checkerboard_sections_urls(self):
        self.base_check_request("get", "autocomplete/series/")

    def test_checkerboard_apartments_urls(self):
        self.base_check_request("get", "autocomplete/company-builder/")

    def test_infra_search_urls(self):
        r = self.base_check_request("get", "infra-search/infra-search/")

        ap_keys = ['id', 'coords', 'name',
                   'promosite_domain']
        for ap in r:
            # check all response objects
            self.assertListEqual(sorted(list(ap.keys())), sorted(ap_keys))

    def test_autocomplete_purchaseconditions_urls(self):
        self.base_check_request("get", "autocomplete/company/")

    def test_autocomplete_markers_urls(self):
        self.base_check_request("get", "autocomplete/purchase-conditions/")

    def test_autocomplete_markers_urls(self):
        self.base_check_request("get", "autocomplete/markers")

    def test_autocomplete_caller_actions_urls(self):
        self.base_check_request("get", "autocomplete/caller_actions/")

    def test_autocomplete_speech_tags_urls(self):
        self.base_check_request("get", "autocomplete/speech_tags/")

    def test_autocomplete_callers_urls(self):
        self.base_check_request("get", "autocomplete/callers/")
