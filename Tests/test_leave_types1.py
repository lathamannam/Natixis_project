from configure.leave_type import LeaveType
from configure.leave_page import LeavePage
from configure.work_week import WorkWeek
import pytest
from leave.driver_management import DriverManager


def test1():
    # 1.lanuch orangehrm application
    # 2.enter valid credential
    # 3.login
    # 4.display the login features
    # 5.click configure
    # 6.display sub parts
    # 7.select leave types
    # 8.click the leave types
    # 9.click add
    # 10.enter name
    # 11.click save button
    driver_mgr = DriverManager()
    obj = LeaveType(driver_mgr.driver)
    obj.leave_type()
    values = obj.get_table_data()
    expected = "hello"
    assert expected in values


def test2():
    #1.lunch orangeHRM application
    #2.enter valid credential
    #3.login
    #4.display the features of orange hrm
    #5.click leave btn.the featuresof btn is display
    #6.click configure open sub modules
    #7.select the leave period and display leave period
    #8.click edit
    #9. leave period page is open
    #10.enter month,date.
    #11.click save button
    driver_mgr = DriverManager()
    obj = LeavePage(driver_mgr.driver)
    expected = "Successfully Saved"
    actual = obj.leave_period()
    assert expected == actual

def test3():
    driver_mgr = DriverManager()
    obj = WorkWeek(driver_mgr.driver)
    expected = "Successfully Saved"
    actual = obj.work_week()
    assert expected == actual














