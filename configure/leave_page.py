from leave.selenium_helper import SeleniumHelper
import time


class LeavePage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        time.sleep(2)

    def leave_period(self):
        element = self.helper.identify_element('menu_leave_viewLeaveModule', 'ID', 'leave')
        self.helper.click(element)
        element1 = self.helper.identify_element("menu_leave_Configure", "ID", "configure")
        self.helper.click(element1)
        element2 = self.helper.identify_element("menu_leave_defineLeavePeriod", "ID", "leaveperiod")
        self.helper.click(element2)
        element3 = self.helper.identify_element('//*[@id="btnEdit"]', "XPATH", "EDIT")
        self.helper.click(element3)
        #time.sleep(5)
        element4 = self.helper.identify_element("btnEdit", "ID", "save")
        self.helper.click(element4)
        #time.sleep(5)
        #element5 = self.helper.identify_element(, "XPATH", "Successfully Saved")

        #return element5



if __name__ == "__main__":
    from leave.driver_management import DriverManager

    driver_mgr = DriverManager()
    obj = LeavePage(driver_mgr.driver)
    obj.leave_period()
