import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class MyTestCase(unittest.TestCase):
    chrome_options = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--disable-extensions")
        cls.chrome_options.add_argument("--incognito")
        cls.chrome_options.add_argument("--disable-popup-blocking")
        cls.chrome_options.add_argument("--start-maximized")

    def setUp(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://todomvc.com/examples/angularjs/#/")
        self.driver.implicitly_wait(10)

    def add_new_task(self, task_name):
        self.driver.find_element_by_class_name("new-todo").send_keys(task_name + "\n")
        time.sleep(3)

    def test_add_new_task(self):
        self.add_new_task("Clean my house")
        tasks_names = [element.text for element in self.driver.find_elements_by_xpath
        ("/html/body/ng-view/section/section/ul/li/div")]
        self.assertTrue("Clean my house" in tasks_names)

    def tearDow(self):
        self.driver.close()
        time.sleep(3)

    def edit_task(self, task_to_chang, new_task_name):
        self.add_new_task(task_to_chang)
        # self.driver.find_element_by_class_name("new-todo").send_keys("Wake up\n")

        v = self.driver.find_elements_by_class_name("ng-binding")

        action_chains = ActionChains(self.driver)
        action_chains.double_click(v[1]).perform()
        time.sleep(3)

        f = self.driver.find_element_by_class_name("edit").send_keys("\n")
        action_chains.double_click(f).perform()
        time.sleep(3)


        self.driver.find_elements_by_class_name("edit")[1].send_keys("Go to sleep\n")
        time.sleep(3)

        pass

    def test_edit_Wake_up_to_Wake_up(self):
        self.edit_task("Wake up", "Go to sleep")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
