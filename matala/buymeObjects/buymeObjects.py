import time
import unittest
from random import random, randint

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class BuyMeObjects:

    def __init__(self, browser_type):
        self.url = "https://buyme.co.il"
        self.browser_type = browser_type
        self.options = self.set_options()
        self.driver = self.set_driver()
        self.open_page()
        self.elements_dict = dict()
        self.fill_elements()
        self.actions = ActionChains(self.driver)

    def set_options(self):
        self.options = Options()
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--start-maximized")
        return self.options

    def set_driver(self):
        if self.browser_type == "chrome":
            return webdriver.Chrome(options=self.options)
        elif self.browser_type == "edge":
            return webdriver.edge

    def open_page(self):
        self.driver.get("https://buyme.co.il")

    def fill_elements(self):
        self.elements_dict["subscribe1"] = self.get_subscribe_element1()
        self.set_subscribe_element1()
        self.elements_dict["subscribe2"] = self.get_subscribe_element2()
        self.set_subscribe_element2()
        self.elements_dict["first_name"] = self.get_first_name()
        self.elements_dict["mail"] = self.get_mail_element()
        self.elements_dict["password"] = self.get_password_element()
        self.elements_dict["password_confirm"] = self.get_password_verification_element()
        self.elements_dict["subscribe"] = self.get_subscribe_element()

    def get_subscribe_element1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_xpath \
            ('//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]')

    def set_subscribe_element1(self):
        self.driver.implicitly_wait(10)
        self.elements_dict["subscribe1"].click()

    def get_subscribe_element2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_xpath \
            ('//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span')

    def set_subscribe_element2(self):
        self.driver.implicitly_wait(10)
        self.elements_dict["subscribe2"].click()

    def get_first_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_css_selector("input[placeholder='שם פרטי']")

    def set_first_name(self, first_name):
        """

        :param first_name:
        :return:
        """
        self.elements_dict["first_name"].send_keys(first_name)

    def get_mail_element(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_css_selector("input[placeholder='מייל']")

    def set_mail_element(self, mail_address):
        self.elements_dict["mail"].send_keys(mail_address)

    def get_password_element(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_css_selector("input[placeholder='סיסמה']")

    def set_password(self, password):
        self.elements_dict["password"].send_keys(password)

    def get_password_verification_element(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_css_selector("input[placeholder='אימות סיסמה']")

    def set_password_verification(self, password):
        self.elements_dict["password_confirm"].send_keys(password)

    def get_page_title(self):
        return self.driver.title

    def get_subscribe_element(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_css_selector("span[class='label']")

    def set_subscribe_element(self):
        self.elements_dict["subscribe"].click()

    def check_subscription(self, firs_name, email_address):
        try:
            self.elements_dict["my_account"] = self.driver.find_element_by_css_selector("li[id='ember1530']")
            self.actions.move_to_element(self.elements_dict["my_account"]).perform()
            self.elements_dict["account_details"] = \
                self.driver.find_element_by_css_selector("a[id='ember1575']")
            self.elements_dict["account_details"].click()
            time.sleep(10)
            print(self.driver.current_url)
            self.driver.implicitly_wait(10)
            print(self.driver.find_element_by_xpath("//*[@id='ember1711']").get_property("value"))
            print(self.driver.find_element_by_xpath("//*[@id='ember1716']").get_property("value"))
        except():
            return "didn't subscribe"

    def close_page(self):
        self.driver.close()


# if __name__ == "__main__":

