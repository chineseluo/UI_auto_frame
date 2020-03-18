#coding:utf-8
import unittest
from selenium import webdriver
from PageObject.home_page import Home_page
class Home_page_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("类后执行一次")

    def setUp(self):
        print("开始执行case")
        self.driver = webdriver.Chrome("D:/chromedriver/chromedriver_win32_75/chromedriver.exe")
        self.home_page = Home_page(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("结束执行case")

    def test_search_01(self):
        self.home_page.get_home_page_url("https://www.ctrip.com")
        self.home_page.search_info("北京")
        self.home_page.switch_driver_to_otherHandle()
        self.assertEqual("北京", self.home_page.get_city_text())


    def test_click_insurance(self):
        self.home_page.get_home_page_url("https://www.ctrip.com")
        self.home_page.click_insurance()
        self.assertEqual("保险公司", self.home_page.get_insurance_text())

if __name__ == "__main__":
    home_page_case = Home_page_case()
    home_page_case.test_search_01()
