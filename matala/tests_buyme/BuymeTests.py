import unittest
from lxml import etree
from buymeObjects import buymeObjects
from random import randint

from buymeObjects.buymeObjects import BuyMeObjects
from tests_buyme.creatConfig import CreateConfig

RANDOM_NUM = randint(1, 10000)
INPUT = {"browser_type": "chrome",
         "url": "https://buyme.co.il",
         "excepted_title": "BUYME אתר המתנות והחוויות הגדול בישראל | Gift Card",
         "first_name": "Shimon",
         'mail': f"S1.h{RANDOM_NUM}@gmail.com",
         "password": f"S1.h{RANDOM_NUM}@gmail.com",
         "password_confirm": f"S1.h{RANDOM_NUM}@gmail.com",
         "subscribed_name": "Shimon",
         "subscribed_email": f"S1.h{RANDOM_NUM}@gmail.com"}


class BuymeTests(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.tree = etree.parse("matala/buymeObjects/config_buy_me_ex").root()

    def test_something(self):
        self.assertEqual(True, False)

    def setUpClass(cls):
        cls.creat_configuration_file()

    @classmethod
    def creat_configuration_file(cls):
        config = CreateConfig("buy_me_website")
        for key, value in INPUT.items():
            config.add_child(key, INPUT[key])
        config.write_to_file("config_buy_me_ex")

    def test_subsection(self):
        c = BuyMeObjects(self.tree.find("browser_type").text)
        c.set_first_name(self.tree.find("first_name").text)
        c.set_mail_element(self.tree.find("email").text)
        c.set_password(self.tree.find("password").text)
        c.set_password_verification(self.tree.find("password_confirm").text)
        c.set_subscribe_element()

    def raed_config(self):
        self.expected_title = self.tree.find("expected_title").text
        print(c.get_page_title())
        print(c.check_subscription(self.tree.find("subscribed_name").text, self.tree.find("subscribed_email").text))


if __name__ == '__main__':
    unittest.main()
