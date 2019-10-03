from selenium import webdriver
import pytest
import unittest

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(executable_path="C:\\Tejas_Work\\Learn\\Selenium drivers\\chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(10)
    #
    def test_loginpage_valid(self):
        browser.get("https://portal.dev.syapse.com")
        print("Into Login Page")




    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()



