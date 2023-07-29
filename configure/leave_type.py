from leave.selenium_helper import SeleniumHelper
import time


class LeaveType:

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)


    def leave_type(self):
        element = self.helper.identify_element('menu_leave_viewLeaveModule', 'ID', 'leave')
        self.helper.click(element)
        element1 = self.helper.identify_element("menu_leave_Configure", "ID", "configure")
        self.helper.click(element1)
        element2 = self.helper.identify_element("menu_leave_Configure", "ID", "configure")
        self.helper.click(element2)
        element3 = self.helper.identify_element("menu_leave_leaveTypeList", "ID", "leavetype")
        self.helper.click(element3)
        time.sleep(2)
        element4 = self.helper.identify_element("btnAdd", "ID", "click")
        self.helper.click(element4)
        element5 = self.helper.identify_element("leaveType_txtLeaveTypeName", "ID", "add")
        self.helper.send_text(element5,"hello")
        element6 = self.helper.identify_element("saveButton", "ID", "save")
        self.helper.click(element6)
        time.sleep(2)

    def get_table_data(self):
        leave_elements = self.helper.identifying_elements("XPATH","//*[@id='resultTable']/tbody/tr/td[2]", "result_table")
        table_data = []
        for elements in leave_elements:
            element = elements.text
            table_data.append(element)
        return table_data


if __name__ == "__main__":
    from leave.driver_management import DriverManager
    driver_mgr = DriverManager()
    obj = LeaveType(driver_mgr.driver)
    obj.leave_type()
    obj.get_table_data()



