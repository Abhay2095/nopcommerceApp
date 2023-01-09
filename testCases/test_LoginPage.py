import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    def test_HomePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()

        else:
            self.driver.close()
            assert False

    def test_LoginPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.close()
            assert False
























