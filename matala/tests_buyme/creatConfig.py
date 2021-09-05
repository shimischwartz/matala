from lxml import etree as Et
from random import randint


RANDOM_NUM = randint(1, 10000)
INPUT = {"browser_type": "chrome",
         "url": "https://buyme.co.il",
         "excepted_title": "BUYME אתר המתנות והחוויות הגדול בישראל | Gift Card",
         "first_name": "Shimon",
         'email': f"S1.h{RANDOM_NUM}@gmail.com",
         "password": f"S1.h{RANDOM_NUM}@gmail.com",
         "password_confirm": f"S1.h{RANDOM_NUM}@gmail.com",
         "subscribed_name": "Shimon",
         "subscribed_email": f"S1.h{RANDOM_NUM}@gmail.com"}

class CreateConfig:

    def __init__(self, root_name):
        self.__root = Et.Element(root_name)
        self.__tree = Et.ElementTree(self.__root)

    def creat_configuration_file(cls):
        config = CreateConfig("buy_me_website")
        for key, value in INPUT.items():
            config.add_child(key, INPUT[key])
        config.write_to_file("config_buy_me_ex")

    def add_child(self, tag_name, text):
        Et.SubElement(self.__root, tag_name).text = text

    def write_to_file(self, file_name):
        self.__tree.write(file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')


