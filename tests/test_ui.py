from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


class _TestMainPage():

    main_url = ""

    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.main_url)

    def test_footer(self):
        footer_list = self.driver.find_elements_by_css_selector(".main-menu_item.menuItem")
        for each in footer_list:
            each.click()
            name = each.text
            footer_list = self.driver.find_elements_by_css_selector(".main-menu_item.menuItem")
            for i in footer_list:
                if i.text == name:
                    footer_list.remove(i)

    def tearDown(self):
        self.driver.close()
