from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import unittest
# print("hello world1")
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://todomvc.com/examples/angularjs/#/")

driver.find_element_by_class_name(str("new-todo")).send_keys("Clean my house\n")

driver.find_element_by_class_name("new-todo").send_keys("Wake up\n")

v = driver.find_elements_by_class_name("ng-binding")

actionChains = ActionChains(driver)
actionChains.double_click(v[1]).perform()

f = driver.find_element_by_class_name("edit").send_keys("\n")
actionChains.double_click().perform()

driver.find_elements_by_class_name("edit")[1].send_keys("Go to sleep\n")



####################################################################################





#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
#
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=chrome_options)
# # driver.get("https://todomvc.com/examples/angularjs/#/")
# #
# # driver.find_element_by_class_name("new-todo").send_keys("Clean my house\n")
# # driver.find_element_by_class_name("new-todo").send_keys("Clean my house\n")
# # driver.find_element_by_class_name("new-todo").send_keys("Clean my house\n")
#
#
#
#
#
# driver.get("http://todomvc.com/examples/angularjs/#/")
# driver.find_element_by_class_name("new-todo").send_keys("Clean my house\n")
