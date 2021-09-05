import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import unittest


class TodoTests:
    print("hello world1")
    driver, action_chains = None, None
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")

    def set_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://todomvc.com/examples/angularjs/#/")
        self.driver.implicitly_wait(10)
        self.action_chains = ActionChains(self.driver)

    def add_new_task(self, task_name):
        self.driver.find_element_by_class_name("new-todo").send_keys(task_name + "\n")

    def check_add_new_task(self, task_name):
        self.set_driver()
        self.add_new_task(task_name)
        to_return = self.find_a_task(task_name) <= 0
        self.driver.close()
        return to_return

    def find_a_task(self, task_name):
        todo_list = self.driver.find_elements_by_xpath("/html/body/ng-view/section/section/ul/li")
        for i in range(len(todo_list)):
            if todo_list[i].text == task_name:
                time.sleep(5)
                return i
        time.sleep(5)
        return -1

    def edit_a_task(self, old_task_name, new_task_name):
        time.sleep(5)
        todo_list = self.driver.find_elements_by_xpath("/html/body/ng-view/section/section/ul/li")
        edit_list = self.driver.find_elements_by_class_name("edit")
        check_list = self.driver.find_elements_by_class_name("toggle")
        i = self.find_a_task(old_task_name)
        self.action_chains.double_click(todo_list[i]).perform()
        for j in range(len(old_task_name)):
            edit_list[i].send_keys("\u0008")
        edit_list[i].send_keys(new_task_name + "\n")
        if check_list[i].is_selected():
            check_list[i].click()

        time.sleep(5)

    def check_edit_a_task(self, old_task_name, new_task_name):
        self.set_driver()
        self.add_new_task(old_task_name)
        index = self.find_a_task(old_task_name)
        self.edit_a_task(old_task_name, new_task_name)
        check_list = self.driver.find_elements_by_class_name("toggle")
        to_return = self.find_a_task(new_task_name) == index and not check_list[index].is_selected()
        self.driver.close()
        return to_return

        # check_list[index].click()
        # print(check_list[index].is_selected(), "rftyui")
        # # check_list = driver.find_elements_by_class_name("toggle")
        # check_list[index].click()
        # print(check_list[index].is_selected(), "rftyui")

    def delete_a_task(self, task_name):
        index = self.find_a_task(task_name)
        self.action_chains.move_to_element(self.driver.find_elements_by_xpath
                                           ("/html/body/ng-view/section/section/ul/li")[index]).perform()
        self.driver.find_elements_by_class_name("destroy")[index].click()

    def check_delete_a_task(self, task_name):
        self.set_driver()
        self.add_new_task(task_name)
        before = self.find_a_task(task_name)
        time.sleep(4)
        self.delete_a_task(task_name)
        to_return = (self.find_a_task(task_name) == -1) and (before >= 0)
        self.driver.close()
        return to_return

    def is_marked(self, index):
        return self.driver.find_elements_by_class_name("toggle")[index].is_selected()

    def mark_task_as_completed(self, task_name):
        index = self.find_a_task(task_name)
        to_mark = self.driver.find_elements_by_class_name("toggle")[index]
        if self.is_marked(index):
            return
        to_mark.click()

    def check_mark_task_as_completed(self, task_name):
        self.set_driver()
        self.add_new_task(task_name)
        index = self.find_a_task(task_name)
        self.mark_task_as_completed(task_name)
        to_return = self.is_marked(index)
        self.driver.close()
        return to_return

    def mark_completed_task_as_active(self, task_name):
        index = self.find_a_task(task_name)
        to_mark = self.driver.find_elements_by_class_name("toggle")[index]
        if to_mark.is_selected():
            to_mark.click()

    def check_mark_completed_task_as_active(self, task_name):
        self.set_driver()
        self.add_new_task(task_name)
        index = self.find_a_task(task_name)
        before_mark = self.is_marked(index)
        self.mark_task_as_completed(task_name)
        after_mark = self.is_marked(index)
        self.mark_completed_task_as_active(task_name)
        after_unmark = self.is_marked(index)
        to_return = (not before_mark) and after_mark and (not after_unmark)
        self.driver.close()
        return to_return

    def clear_completed_tasks(self):
        self.driver.find_element_by_class_name("clear-completed").click()

    def check_clear_completed_tasks \
                    (self, task_for_uncompleted, task_for_completed):
        self.set_driver()
        self.add_new_task(task_for_uncompleted)
        self.add_new_task(task_for_completed)
        self.mark_task_as_completed(task_for_completed)
        index = self.find_a_task(task_for_completed)
        self.clear_completed_tasks()
        to_return = index >= 0 and self.find_a_task(task_for_completed) == -1
        self.driver.close()
        return to_return

    def check_see_different_views(self, tasks):
        self.check_view_all(tasks[0], tasks[1])
        self.check_view_active(tasks[0], tasks[1])
        self.check_view_completed(tasks[0], tasks[1])

    def check_view_all(self, task_for_uncompleted, task_for_completed):
        self.set_driver()
        self.add_new_task(task_for_uncompleted)
        self.add_new_task(task_for_completed)
        self.switch_to_view_active()
        self.switch_to_view_all()
        to_return = self.find_a_task(task_for_uncompleted) <= 0 and \
               self.find_a_task(task_for_completed) <= 0
        self.driver.close()
        return to_return

    def check_view_active(self, task_for_uncompleted, task_for_completed):
        self.set_driver()
        self.add_new_task(task_for_uncompleted)
        self.add_new_task(task_for_completed)
        self.switch_to_view_active()
        to_return = self.find_a_task(task_for_uncompleted) <= 0 and \
                    self.find_a_task(task_for_completed) == -1
        self.driver.close()
        return to_return


    def switch_to_view_all(self):
        self.driver.find_element_by_xpath("/html/body/ng-view/section/footer/ul/li[1]")[1].click()

    def switch_to_view_active(self):
        self.driver.find_element_by_xpath("/html/body/ng-view/section/footer/ul/li[1]")[2].click()

    def switch_to_view_completed(self):
        self.driver.find_element_by_xpath("/html/body/ng-view/section/footer/ul/li[1]")[3].click()
    #
    #
    #
    ###################################################################################
    #
    #
    #
    #
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


if __name__ == '__main__':
    todo_tests = TodoTests()
    # print("Add a new task test is: ", todo_tests.check_add_new_task("Clean my house"))
    # print("Edit a task is: ", todo_tests.check_edit_a_task("Wake up", "Go to sleep"))
    # print("Delete a task is: ", todo_tests.check_delete_a_task("Wake up"))
    print("Mark task as completed is: ", todo_tests.check_mark_task_as_completed("Wake up"))
    print("Mark completed task as active is: ", todo_tests.check_mark_completed_task_as_active("Wake up"))
    print("Clear completed tasks is: ", todo_tests.check_clear_completed_tasks("Wake up", "Clean the house"))
