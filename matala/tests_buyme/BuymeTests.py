import unittest
from lxml import etree
from buymeObjects import buymeObjects
from random import randint

from buymeObjects.buymeObjects import BuyMeObjects
from tests_buyme.creatConfig import CreateConfig

RANDOM_NUM = randint(1, 10000)
INPUT = {"browser_type": "chrome",
         "url": "https://buyme.co.il",
         "excepted_title": "title_to_insert",
         "first_name": "Shimon",
         'mail': f"S1.h{RANDOM_NUM}@gmail.com",
         "password": f"S1.h{RANDOM_NUM}@gmail.com",
         "password_confirm": f"S1.h{RANDOM_NUM}@gmail.com"}


class BuymeTests(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    def creat_configuration_file(self):
        config = CreateConfig("buy_me_website")
        for key, value in INPUT.items():
            config.add_child(key, INPUT[key])
        config.write_to_file("config_buy_me_ex")

    def raed_config(self):
        self.tree = etree.parse("matala/buymeObjects/config_buy_me_ex").root()
        self.browser_type = self.tree.find("browser_type").text
        self.expected_title = self.tree.find("expected_title").text
        firs_name = self.tree.find("first_name").text
        password = self.tree.find("password").text
        password_confirm = self.tree.find("password_confirm").text
        c = BuyMeObjects("chrome")
        c.set_first_name("Shimon")

        c.set_mail_element()
        c.set_password()
        c.set_password_verification(f"S1.h{new_num}@gmail.com")
        c.set_subscribe_element()
        print(c.get_page_title())
        print(c.check_subscription("Shimon", f"S1.h{new_num}@gmail.com"))


if __name__ == '__main__':
    unittest.main()
