from leave.selenium_helper import SeleniumHelper
import time

class LeavePage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        time.sleep(2)

    def holidays(self):
        element = self.helper.identify_element('menu_leave_viewLeaveModule', 'ID', 'leave')
        self.helper.click(element)
        element = self.helper.identify_element("menu_leave_Configure", "ID", "configure")
        self.helper.click(element)
        element = self.helper.identify_element("menu_leave_viewHolidayList", "ID", "holidays")
        self.helper.click(element)
        calender=self.helper.identify_element('//*[@id="frmHolidaySearch"]/fieldset/ol/li[1]/img','XPATH','ELE')
        self.helper.click(calender)
        year=self.helper.identify_element('//*[@id="ui-datepicker-div"]/div/div/select[2]','XPATH','ele2')
        self.helper.click(year)
        self.helper.selecting_element(year,'2021')

        month=self.helper.identify_element('//*[@id="ui-datepicker-div"]/div/div/select[1]','XPATH','ele3')
        self.helper.click(month)
        self.helper.selecting_element(month,'May')
        time.sleep(3)
        date=self.helper.identifying_elements('//*[@id="ui-datepicker-div"]/table/tbody/tr/td','XPATH','ele6')
        self.helper.calendar_to_date(date,'22')



        """
        element = self.helpr.identify_element("calFromDate", "ID", "from")
        self.helper.send_text(element, "2020-9-22 ")
        element = self.helper.identify_element("calToDate", "ID", "TO")
        self.helper.clear_test(element)
        element = self.helper.identify_element("calToDate", "ID", "TO")
        self.helper.send_text(element, "2020-11-27")
        element = self.helper.identify_element("btnAdd", "ID", "add")
        self.helper.click(element)
        element = self.helper.identify_element("holiday_description", "ID", "name")
        self.helper.send_text(element, "puhspa")
        element1 = self.helper.identify_element("holiday_date", "id", "date")
        self.helper.click(element1)
        self.helper.clear_test(element1)
        #element = self.helper.identify_element("holiday_date", "ID", "date")
        self.helper.send_text(element1,"2021-9-12")
        element = self.helper.identify_element("holiday_recurring", "ID", "click")
        self.helper.click(element)
        element = self.helper.identify_element("holiday_length", "ID", "drop")
        self.helper.selecting_element(element, "Full Day")
        element = self.helper.identify_element("saveBtn", "ID", "save")
        self.helper.click(element)
        time.sleep(2)"""
if __name__ == "__main__":
    from leave.driver_management import DriverManager
    driver_mgr = DriverManager()
    obj = LeavePage(driver_mgr.driver)
    obj.holidays()



