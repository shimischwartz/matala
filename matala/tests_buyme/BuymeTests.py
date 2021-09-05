import unittest
from lxml import etree
from buymeObjects import buymeObjects
from random import randint
from buymeObjects.buymeObjects import BuyMeObjects
from tests_buyme.creatConfig import CreateConfig


class BuymeTests(unittest.TestCase):
    tree = None
    objects = None

    @classmethod
    def setUpClass(cls):        cls.tree = etree.parse("config_buy_me_ex").getroot()



    def test_something(self):
        self.assertEqual(True, True)

    def test_subscription(self):
        self.subscription()
        self.assertTrue(self.objects.check_subscription())
        self.assertEqual(self.tree.find("first_name").text, self.objects.get_subscribed_first_name())
        self.assertEqual(self.tree.find("email").text, self.objects.get_subscribed_email_address())

    def subscription(self):
        self.objects = BuyMeObjects(self.tree.find("browser_type").text)
        self.objects.set_first_name(self.tree.find("first_name").text)
        self.objects.set_mail_element(self.tree.find("email").text)
        self.objects.set_password(self.tree.find("password").text)
        self.objects.set_password_verification(self.tree.find("password_confirm").text)
        self.objects.set_subscribe_element()


if __name__ == '__main__':
    unittest.main()
