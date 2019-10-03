from selenium import webdriver
import unittest

class LoginPage_PO(unittest.TestCase):

    def __init__(self,browser):
        self.browser = browser
        self.username_textbox_xpath = "//input[@name = 'email']"
        self.password_textbox_xpath = "//input[@name = 'password']"
        self.signin_buttom_xpath = "//button[@type= 'submit']"



    def enter_username(self,username):
        self.browser.




