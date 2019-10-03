from selenium import webdriver
from MTB_Pages.Base_TestClass.TestBase import TestBase
from MTB_Pages.MTB_Pages.PO_Login import LoginPage_PO
import unittest
class Login_TC(unittest.TestCase):


    def browserInit(self):
        TB = TestBase.setUpClass()
        print("Browser is opened")


    def login_page(self):
        login = LoginPage_PO.


