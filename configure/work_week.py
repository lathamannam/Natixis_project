from leave.selenium_helper import SeleniumHelper
import time

class WorkWeek:

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        time.sleep(2)

    def work_week(self):
        element = self.helper.identify_element('menu_leave_viewLeaveModule', 'ID', 'leave')
        self.helper.click(element)
        element1 = self.helper.identify_element("menu_leave_Configure", "ID", "configure")
        self.helper.click(element1)
        element2= self.helper.identify_element("menu_leave_defineWorkWeek", "ID", "work week")
        self.helper.click(element2)
        element3 = self.helper.identify_element("saveBtn", "ID", "EDIT")
        self.helper.click(element3)
        element4 = self.helper.identify_element("saveBtn", "ID", "SAVE")
        self.helper.click(element4)
        time.sleep(2)

if __name__== "__main__":
    from leave.driver_management import DriverManager
    driver_mgr = DriverManager()
    obj = WorkWeek(driver_mgr.driver)
    obj.work_week()


