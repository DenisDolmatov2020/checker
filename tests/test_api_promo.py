from tests.base import BaseUnitTest


class TestUrls(BaseUnitTest):
    """

    """
    TEST_API_HOST = ""
    TEST_API_PORT = ""
    TEST_API_VERSION = ""

    # def test_base_url(self):

    # self.base_check_request("get", "/")
    # self.base_check_request("get", "api/mainsearchform/")
    # self.base_check_request("get", "api/location/")
    # self.base_check_request("get", "api/apartmentsearchform/")
    # self.base# _check_request("get", "api/companytype/")
    # self.base_check_request("get", "api/apartment/")
    # self.base_check_request("get", "api/complexsearchform/")
    # self.base_check_request("get", "api/company/")

    def test_urls(self):
        self.base_check_request("get", "apartments-page/")
        self.base_check_request("get", "purchase-conditions-page/")

        # self.base_check_request("get", "housing-page/1/")
        self.base_check_request("get", "actions-page/")
        self.base_check_request("get", "building-stages-page/")
        self.base_check_request("get", "contacts-page/")
        self.base_check_request("get", "404-page/")
        self.base_check_request("get", "apartments/")
        self.base_check_request("get", "pages/")
        # self.base_check_request("get", "robots/")
        # self.base_check_request("get", "favicon-url/")
        # self.base_check_request("get", "sitemap/")

    def test_apartment_page_urls(self):
        """
           Test complexes url
       """
        r = self.base_check_request("get", "apartments-page/")

        cpx_keys = ['id', 'menu', 'complexName', 'workingHoursFrom', 'workingHoursTo', 'federalLaw', 'metaTitle',
                    'metaDescription', 'metaKeywords', 'phone', 'address', 'logoUrl', 'phonecallScript',
                    'phonecallReplaceScript', 'phonecallReplaceSrc', 'webmasterVerificationPanels', 'socialLinks',
                    'counters', 'favicon',
                    'showLogo', 'showPhone',
                    'showTitle', 'companyLogoUrl', 'scripts', 'noscripts', 'content',
                    'companyName',
                    'typePrepName']

        # for c in r:

        # check response objects structure
        self.assertListEqual(sorted(list(r.keys())), sorted(cpx_keys))

        # check response types
        self.assertIsInstance(r['id'], int)

        # self.assertIsInstance(r['menu'], str)
        self.assertIsInstance(r['complexName'], str)
        self.assertIsInstance(r['workingHoursFrom'], int)
        self.assertIsInstance(r['workingHoursTo'], int)
        self.assertIsInstance(r['federalLaw'], str)
        self.assertIsInstance(r['metaTitle'], str)
        self.assertIsInstance(r['metaDescription'], str)
        self.assertIsInstance(r['metaKeywords'], str)
        self.assertIsInstance(r['phone'], str)
        self.assertIsInstance(r['address'], str)
        self.assertIsInstance(r['logoUrl'], str)
        self.assertIsInstance(r['phonecallScript'], str)
        self.assertIsInstance(r["phonecallReplaceScript"], str)
        self.assertIsInstance(r["phonecallReplaceSrc"], str)
        # self.assertIsInstance(r['webmasterVerificationPanels'], dict)
        # self.assertIsInstance(r['socialLinks'], dict)
        # self.assertIsInstance(r['counters'], dict) # counters
        # self.assertIsInstance(r['favicon'], str)  # dicts
        # self.assertIsInstance(r['showLogo'], bool)  # counters
        # self.assertIsInstance(r['showPhone'], bool)  # dicts
        # self.assertIsInstance(r['showTitle'], bool)
        # self.assertIsInstance(r['companeLogOutUrl'], str)
        # self.assertIsInstance(r['scripts'], dict)
        # self.assertIsInstance(r['noscripts'], dict)
        # self.assertIsInstance(r['content'], dict)
        # self.assertIsInstance(r['companyName'], str)
        # self.assertIsInstance(r['typePrepare'], str)

    def test_main_page(self):
        r = self.base_check_request("get", "main-page/")

        cpx_keys = ['id', 'menu', 'complexName', 'workingHoursFrom', 'workingHoursTo', 'federalLaw', 'metaTitle',
                    'metaDescription', 'metaKeywords', 'phone', 'address', 'logoUrl', 'phonecallScript',
                    'phonecallReplaceScript', 'phonecallReplaceSrc', 'webmasterVerificationPanels', 'socialLinks',
                    'counters', 'favicon',
                    'showLogo', 'showPhone' \
            , 'showTitle', 'companyLogoUrl', 'scripts', 'noscripts', 'content' \
            , 'companyName',
                    'typePrepName']
        # check response objects structure
        self.assertListEqual(sorted(list(r.keys())), sorted(cpx_keys))

        # check response types
        self.assertIsInstance(r['id'], int)

        # self.assertIsInstance(r['menu'], str)
        self.assertIsInstance(r['complexName'], str)
        self.assertIsInstance(r['workingHoursFrom'], int)
        self.assertIsInstance(r['workingHoursTo'], int)
        self.assertIsInstance(r['federalLaw'], str)
        self.assertIsInstance(r['metaTitle'], str)
        self.assertIsInstance(r['metaDescription'], str)
        self.assertIsInstance(r['metaKeywords'], str)
        self.assertIsInstance(r['phone'], str)
        self.assertIsInstance(r['address'], str)
        self.assertIsInstance(r['logoUrl'], str)
        self.assertIsInstance(r['phonecallScript'], str)
        self.assertIsInstance(r["phonecallReplaceScript"], str)
        self.assertIsInstance(r["phonecallReplaceSrc"], str)

    def test_project_page(self):
        r = self.base_check_request("get", "project-page/")

        cpx_keys = ['id', 'menu', 'complexName', 'workingHoursFrom', 'workingHoursTo', 'federalLaw', 'metaTitle',
                    'metaDescription', 'metaKeywords', 'phone', 'address', 'logoUrl', 'phonecallScript',
                    'phonecallReplaceScript', 'phonecallReplaceSrc', 'webmasterVerificationPanels', 'socialLinks',
                    'counters', 'favicon',
                    'showLogo', 'showPhone' \
            , 'showTitle', 'companyLogoUrl', 'scripts', 'noscripts', 'content' \
            , 'companyName',
                    'typePrepName']

        # for c in r:

        # check response objects structure
        self.assertListEqual(sorted(list(r.keys())), sorted(cpx_keys))

        # check response types
        self.assertIsInstance(r['id'], int)

        # self.assertIsInstance(r['menu'], str)
        self.assertIsInstance(r['complexName'], str)
        self.assertIsInstance(r['workingHoursFrom'], int)
        self.assertIsInstance(r['workingHoursTo'], int)
        self.assertIsInstance(r['federalLaw'], str)
        self.assertIsInstance(r['metaTitle'], str)
        self.assertIsInstance(r['metaDescription'], str)
        self.assertIsInstance(r['metaKeywords'], str)
        self.assertIsInstance(r['phone'], str)
        self.assertIsInstance(r['address'], str)
        self.assertIsInstance(r['logoUrl'], str)
        self.assertIsInstance(r['phonecallScript'], str)
        self.assertIsInstance(r["phonecallReplaceScript"], str)
        self.assertIsInstance(r["phonecallReplaceSrc"], str)

    def test_actions_page(self):
        r = self.base_check_request("get", "actions-page/")

        cpx_keys = ['id', 'menu', 'complexName', 'workingHoursFrom', 'workingHoursTo', 'federalLaw', 'metaTitle',
                    'metaDescription', 'metaKeywords', 'phone', 'address', 'logoUrl', 'phonecallScript',
                    'phonecallReplaceScript', 'phonecallReplaceSrc', 'webmasterVerificationPanels', 'socialLinks',
                    'counters', 'favicon',
                    'showLogo', 'showPhone' \
                    ,'showTitle', 'companyLogoUrl', 'scripts', 'noscripts', 'content' \
                    ,'companyName','typePrepName']

        # for c in r:

        # check response objects structure
        self.assertListEqual(sorted(list(r.keys())), sorted(cpx_keys))

        # check response types
        self.assertIsInstance(r['id'], int)

        # self.assertIsInstance(r['menu'], str)
        self.assertIsInstance(r['complexName'], str)
        self.assertIsInstance(r['workingHoursFrom'], int)
        self.assertIsInstance(r['workingHoursTo'], int)
        self.assertIsInstance(r['federalLaw'], str)
        self.assertIsInstance(r['phone'], str)
        self.assertIsInstance(r['address'], str)
        self.assertIsInstance(r['logoUrl'], str)
        self.assertIsInstance(r['phonecallScript'], str)
        self.assertIsInstance(r["phonecallReplaceScript"], str)
        self.assertIsInstance(r["phonecallReplaceSrc"], str)

    def test_pages(self):

        r = self.base_check_request("get", "/pages/")

        cpx_keys = ['housing', 'purchaseConditions', 'contacts', 'apartments', 'main', 'actions', 'apartment',
                    'buildingStages', 'project']

        # check response objects structure
        self.assertListEqual(sorted(list(r.keys())), sorted(cpx_keys))

    def test_purchase_conditions_page(self):
        r = self.base_check_request("get", "actions-page/")

        cpx_keys = ['id', 'menu', 'complexName', 'workingHoursFrom', 'workingHoursTo', 'federalLaw', 'metaTitle',
                    'metaDescription', 'metaKeywords', 'phone', 'address', 'logoUrl', 'phonecallScript',
                    'phonecallReplaceScript', 'phonecallReplaceSrc', 'webmasterVerificationPanels', 'socialLinks',
                    'counters', 'favicon',
                    'showLogo', 'showPhone',
                    'showTitle', 'companyLogoUrl', 'scripts', 'noscripts', 'content',
                    'companyName', 'typePrepName']

        # check response objects structure
        self.assertListEqual(sorted(list(r.keys())), sorted(cpx_keys))

        # check response types
        self.assertIsInstance(r['id'], int)

        # self.assertIsInstance(r['menu'], str)
        self.assertIsInstance(r['complexName'], str)
        self.assertIsInstance(r['workingHoursFrom'], int)
        self.assertIsInstance(r['workingHoursTo'], int)
        self.assertIsInstance(r['federalLaw'], str)
        self.assertIsInstance(r['phone'], str)
        self.assertIsInstance(r['address'], str)
        self.assertIsInstance(r['logoUrl'], str)
        self.assertIsInstance(r['phonecallScript'], str)
        self.assertIsInstance(r["phonecallReplaceScript"], str)
        self.assertIsInstance(r["phonecallReplaceSrc"], str)