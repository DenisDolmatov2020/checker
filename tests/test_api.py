import pytest

from tests.base import BaseUnitTest


class TestUrlsNew(BaseUnitTest):
    """
    """
    TEST_API_HOST = ""
    TEST_API_PORT = ""
    TEST_API_VERSION = "v1.0"

    def setup_module(self):
        # init_something()
        pass

    def teardown_module(self):
        # teardown_something()
        pass

    def test_urls(self):
        """
        Test all API urls
        """
        self.base_check_request("get", "/")
        self.base_check_request("get", "apartments/")
        self.base_check_request("get", "complexes/")
        self.base_check_request("get", "locations/")
        self.base_check_request("get", "companies/")
        self.base_check_request("get", "companies-types/")

        self.base_check_request("get", "count/apartments/")
        self.base_check_request("get", "count/complexes/")

        self.base_check_request("get", "search-forms/apartments/")
        self.base_check_request("get", "search-forms/complexes/")
        self.base_check_request("get", "search-forms/main/")

        self.base_check_request("get", "autocomplete/companies/")
        self.base_check_request("get", "autocomplete/complexes/")
        self.base_check_request("get", "autocomplete/locations/")

        self.base_check_request("get", "apartments_for_maps/?count=1&fields=lat,lon")
        # self.base_check_request("get", "reserve/")
        # self.base_check_request("get", "complain/")
        # self.base_check_request("post", "apartment-complain/")
        # self.base_check_request("post", "order-apartment/")

    @pytest.mark.xfail
    def test_base_url(self):
        """
        Test base API url
        """
        r = self.base_check_request("get", "/")

        base_urls = {
            'apartments': self.build_url('apartments/'),
            'companies': self.build_url('companies/'),
            'companies-types': self.build_url('companies-types/'),
            'complexes': self.build_url('complexes/'),
            'locations': self.build_url('locations/')
        }
        self.assertDictEqual(r, base_urls)

    def test_apartments_url(self):
        """
        Test apartments url
        """
        r = self.base_check_request("get", "apartments")

        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 12, "Invalid default page size")

        ap_keys = ['address', 'building_floors', 'building_type',
                   'company_apartments_count', 'company_id', 'description_small',
                   'floor', 'housing_apartments_count', 'id', 'images', 'lat',
                   'location_ids', 'lon', 'metro_stations', 'price', 'railway_stations',
                   'rooms_count', 'tags', 'template_id', 'title', 'total_area',
                   'updated']
        for ap in r:
            # check all response objects
            self.assertListEqual(sorted(list(ap.keys())), ap_keys)

            # check reseponse types
            self.assertIsInstance(ap["address"], str)
            self.assertIsInstance(ap['building_floors'], int)
            self.assertIsInstance(ap['building_type'], dict)
            self.assertListEqual(sorted(list(ap['building_type'].keys())),
                                 ["id", "name"])
            self.assertIsInstance(ap['company_apartments_count'], int)
            self.assertIsInstance(ap['company_id'], int)
            self.assertIsInstance(ap['description_small'], (str, type(None)))
            self.assertIsInstance(ap['floor'], int)
            self.assertIsInstance(ap['housing_apartments_count'], int)
            self.assertIsInstance(ap['id'], int)
            # self.assertIsInstance(ap['images'], int)
            self.assertIsInstance(ap['lat'], (float, type(None)))
            self.check_list_items_type(ap['location_ids'], int)
            self.assertIsInstance(ap['lon'], (float, type(None)))
            self.check_list_item_keys(ap["metro_stations"],
                                      ['car', 'feet', 'id', 'name', 'public'])
            self.assertIsInstance(ap['price'], int)
            self.assertIsInstance(ap['railway_stations'], list)
            self.assertEqual(ap['railway_stations'], [])
            self.assertIsInstance(ap['rooms_count'], int)
            self.assertIsInstance(ap['tags'], list)
            self.assertEqual(ap['tags'], [])
            self.assertIsInstance(ap['template_id'], int)
            self.assertIsInstance(ap['title'], str)
            self.assertIsInstance(ap['total_area'], float)
            self.assertIsInstance(ap['updated'], (str, type(None)))

    def test_complexes_url(self):
        """
        Test complexes url
        """
        r = self.base_check_request("get", "complexes")

        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 12, "Invalid default page size")

        cpx_keys = ['address', 'apartment_info', 'company_id', 'description',
                    'has_completed_buildings', 'id', 'images', 'is_finished',
                    'klass_type', 'lat', 'location_ids', 'lon', 'metro_stations',
                    'name', 'pinned', 'promo_site_url', 'rooms_count', 'tags', 'term_gc',
                    'term_quarter']

        for c in r:
            # check response objects structure
            self.assertListEqual(sorted(list(c.keys())), cpx_keys)

            # check response types
            self.assertIsInstance(c['address'], str)
            self.check_list_item_keys(c["apartment_info"],
                                      ['code', 'max_price', 'min_price', 'name', 'rooms'])
            self.assertIsInstance(c['company_id'], int)
            self.assertIsInstance(c['description'], (str, type(None)))
            self.assertIsInstance(c['has_completed_buildings'], bool)
            self.assertIsInstance(c['id'], int)
            self.assertIsInstance(c['images'], dict)
            self.assertIsInstance(c['is_finished'], bool)
            self.assertIsInstance(c['klass_type'], (str, type(None)))
            self.assertIsInstance(c['lat'], float)
            self.check_list_items_type(c['location_ids'], int)
            self.assertIsInstance(c['lon'], float)
            self.check_list_item_keys(c["metro_stations"],
                                      ['car', 'feet', 'id', 'name', 'public'])
            self.assertIsInstance(c['name'], str)
            self.assertIsInstance(c['promo_site_url'], str)
            self.check_list_items_type(c['rooms_count'], int)
            self.assertIsInstance(c['tags'], list)
            self.assertEqual(c['tags'], [])
            self.assertIsInstance(c['term_gc'], int)
            self.assertIsInstance(c['term_quarter'], int)

    def test_locations_url(self):
        """
        Test locations url
        """
        r = self.base_check_request("get", "locations")

        self.assertEqual(r, {}, "Expected empty response")

    @pytest.mark.xfail
    def test_companies_url(self):
        """
        Test companies url
        """
        r_keys = ['count', 'next', 'previous', 'results']
        r = self.check_request_keys("get", "companies", r_keys)

        self.assertIsInstance(r['count'], int)
        self.assertIsInstance(r['next'], str)
        self.assertIsInstance(r['previous'], type(None))

        self.assertEqual(len(r["results"]), 12, "Invalid default page size")

        c_keys = ['active_projects', 'address', 'completed_projects', 'description',
                  'email', 'file_name', 'id', 'list_logo', 'list_logo_url', 'logo',
                  'logo_url', 'name', 'phones', 'prices_info', 'rating',
                  'sale_flats', 'sale_townhouses', 'types']
        for c in r["results"]:
            # check all response objects
            self.assertListEqual(sorted(list(c.keys())), sorted(c_keys))

            # check objects structure
            self.assertIsInstance(c['active_projects'], int)
            self.assertIsInstance(c['address'], str)
            self.assertIsInstance(c['completed_projects'], int)
            self.assertIsInstance(c['description'], str)
            self.assertIsInstance(c['email'], str)
            self.assertIsInstance(c['file_name'], (str, type(None)))
            self.assertIsInstance(c['id'], int)
            self.assertIsInstance(c['list_logo'], str)
            self.assertIsInstance(c['list_logo_url'], str)
            self.assertIsInstance(c['logo'], str)
            self.assertIsInstance(c['logo_url'], str)
            self.assertIsInstance(c['name'], str)
            self.check_list_items_type(c['phones'], str)
            self.check_list_item_keys(c["prices_info"], ['price', 'name'], allow_empty=True)
            self.assertIsInstance(c['rating'], dict)
            if c["rating"] != {}:
                self.assertListEqual(sorted(list(c['rating'].keys())),
                                     ['debt_load', 'history', 'reliability', 'transparency'])

            self.assertIsInstance(c['sale_flats'], int)
            self.assertIsInstance(c['sale_townhouses'], int)
            self.check_list_item_keys(c["types"], ['id', 'name'])

    def test_companies_types_url(self):
        """
        Test companies_types url
        """
        r = self.base_check_request("get", "companies-types")
        self.assertIsInstance(r, list)

        # self.assertEqual(len(r), 12, "Invalid default page size")

        ct_keys = ['companies_count', 'id', 'name_plural', 'short_name_plural']
        for ct in r:
            # check response objects structure
            self.assertListEqual(sorted(list(ct.keys())), sorted(ct_keys))

            # check response types
            self.assertIsInstance(ct['name_plural'], str)
            self.assertIsInstance(ct['short_name_plural'], str)
            self.assertIsInstance(ct['id'], int)

    def test_count_apartments_urls(self):
        """
        Check count apartments url
        """
        r = self.base_check_request("get", "count/apartments/")
        self.assertIsInstance(r, dict)
        self.assertIsInstance(r['count'], int)

    def test_count_complexes_urls(self):
        """
        Check count complexes url
        """
        r = self.base_check_request("get", "count/complexes/")
        self.assertIsInstance(r, dict)
        self.assertIsInstance(r['count'], int)

    def test_search_form_apartments_urls(self):
        """
        Check apartments search form url
        """
        r_keys = ['balcony_types', 'bathroom_type', 'building_floors_max',
                  'building_floors_min', 'building_type', 'decoration',
                  'elevators_type', 'floor_max', 'floor_min', 'infrastructure',
                  'living_area_max', 'living_area_min', 'metro_stations',
                  'price_per_m_max', 'price_per_m_min', 'regions', 'rooms_count',
                  'total_area_max', 'total_area_min']
        r = self.check_request_keys("get", "search-forms/apartments/", r_keys)

        self.check_list_item_keys(r["balcony_types"], ['id', 'name'])
        self.check_list_item_keys(r["bathroom_type"], ['id', 'name'])
        self.assertIsInstance(r['building_floors_max'], int)
        self.assertIsInstance(r['building_floors_min'], int)
        self.check_list_item_keys(r["building_type"], ['id', 'name'])
        self.assertIsInstance(r['decoration'], list)
        self.assertEqual(r['decoration'], [])
        self.check_list_item_keys(r["elevators_type"], ['id', 'name'])
        self.assertIsInstance(r['floor_max'], int)
        self.assertIsInstance(r['floor_min'], int)
        self.assertIsInstance(r['infrastructure'], list)
        self.assertEqual(r['infrastructure'], [])
        self.assertIsInstance(r['living_area_max'], int)
        self.assertIsInstance(r['living_area_min'], int)
        self.check_list_item_keys(r["metro_stations"], ['id', 'name'])
        self.assertIsInstance(r['price_per_m_max'], int)
        self.assertIsInstance(r['price_per_m_min'], int)
        self.check_list_item_keys(r["regions"], ['format', 'id', 'locations', 'name', 'slug', 'typeBeforeLocation',
                                                 'typeName', 'typePrepositionalShortName', 'typeShortName'])
        self.check_list_items_type(r['rooms_count'], int)
        self.assertIsInstance(r['total_area_max'], int)
        self.assertIsInstance(r['total_area_min'], int)

    def test_search_form_complexes_urls(self):
        """
        Check complexes search form url
        """
        r_keys = ['balcony_types', 'bathroom_type', 'building_floors_max',
                  'building_floors_min', 'building_type', 'decoration',
                  'elevators_type', 'floor_max', 'floor_min', 'infrastructure',
                  'living_area_max', 'living_area_min', 'metro_stations',
                  'price_per_m_max', 'price_per_m_min', 'regions', 'rooms_count',
                  'term_gc_max', 'term_gc_min', 'total_area_max', 'total_area_min']
        r = self.check_request_keys("get", "search-forms/complexes/", r_keys)

        self.check_list_item_keys(r["balcony_types"], ['id', 'name'])
        self.check_list_item_keys(r["bathroom_type"], ['id', 'name'])
        self.assertIsInstance(r['building_floors_max'], int)
        self.assertIsInstance(r['building_floors_min'], int)
        self.check_list_item_keys(r["building_type"], ['id', 'name'])
        self.assertIsInstance(r['decoration'], list)
        self.assertEqual(r['decoration'], [])
        self.check_list_item_keys(r["elevators_type"], ['id', 'name'])
        self.assertIsInstance(r['floor_max'], int)
        self.assertIsInstance(r['floor_min'], int)
        self.assertIsInstance(r['infrastructure'], list)
        self.assertEqual(r['infrastructure'], [])
        self.assertIsInstance(r['living_area_max'], int)
        self.assertIsInstance(r['living_area_min'], int)
        self.check_list_item_keys(r["metro_stations"], ['id', 'name'])
        self.assertIsInstance(r['price_per_m_max'], int)
        self.assertIsInstance(r['price_per_m_min'], int)
        self.check_list_item_keys(r["regions"],
                                  ['format', 'id', 'locations', 'name', 'slug', 'typeBeforeLocation',
                                   'typeName', 'typePrepositionalShortName', 'typeShortName'])
        self.check_list_items_type(r['rooms_count'], int)
        self.assertIsInstance(r['term_gc_max'], int)
        self.assertIsInstance(r['term_gc_min'], int)


    def test_search_form_main_urls(self):
        """
        Check main search form url
        """
        r_keys = ['price_max', 'price_min', 'rooms_count']
        r = self.check_request_keys("get", "search-forms/main/", r_keys)

        self.assertIsInstance(r['price_min'], int)
        self.assertIsInstance(r['price_max'], int)
        self.check_list_items_type(r['rooms_count'], int)

    def test_autocomplete_companies_urls(self):
        """
        Check autocomplete companies url
        """
        r = self.base_check_request("get", "autocomplete/companies/")
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 10, "Invalid default count")

        ac_keys = ['id', 'name', 'type_name']
        for ac in r:
            # check response objects structure
            self.assertListEqual(sorted(list(ac.keys())), ac_keys)

            # check response types
            self.assertIsInstance(ac['name'], str)
            self.assertIsInstance(ac['type_name'], str)
            self.assertIsInstance(ac['id'], int)

    def test_autocomplete_complexes_urls(self):
        """
        Check autocomplete complexes url
        """
        r = self.base_check_request("get", "autocomplete/complexes/")
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 10, "Invalid default count")

        ac_keys = ['id', 'name', 'type_name']
        for ac in r:
            # check response objects structure
            self.assertListEqual(sorted(list(ac.keys())), ac_keys)

            # check response types
            self.assertIsInstance(ac['name'], str)
            self.assertIsInstance(ac['type_name'], str)
            self.assertIsInstance(ac['id'], int)

    def test_autocomplete_locations_urls(self):
        """
        Check autocomplete locations url
        """
        r = self.base_check_request("get", "autocomplete/locations/")
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 10, "Invalid default count")

        ac_keys = ['ancestors', 'id', 'is_region', 'name', 'prepositional_name',
                   'slug', 'text_for_apartments_search',
                   'text_for_complexes_search', 'type_name']
        # ac_keys_full = ac_keys + ["metro_stations"]
        for ac in r:
            # check response objects structure
            self.assertListEqual(sorted(list(ac.keys())), ac_keys)

            # check response types
            # self.check_list_item_keys(ac["ancestors"], ac_keys_full)
            self.assertIsInstance(ac['id'], int)
            self.assertIsInstance(ac['is_region'], bool)
            self.assertIsInstance(ac['name'], str)
            self.assertIsInstance(ac['prepositional_name'], str)
            self.assertIsInstance(ac['slug'], str)
            self.assertIsInstance(ac['text_for_apartments_search'], (str, type(None)))
            self.assertIsInstance(ac['text_for_complexes_search'], (str, type(None)))
            self.assertIsInstance(ac['type_name'], str)
