import unittest


class MyTestCase(unittest.TestCase):
    my_driver = None

    def setUpClass(self):
        input = input("pleas..")
        # if input == "1":
        #     # open_kikar_hshabat_chrome()
        # else:
        #     # open_kikar_hshabat_edge()
        #
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()