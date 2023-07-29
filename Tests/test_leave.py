from leave.driver_management import DriverManager
from configure.leave_page import LeavePage


def test1():
    try:
        driver_mgr = DriverManager()
        expected_title = "OrangeHRM"
        assert expected_title == driver_mgr.driver.title
    except:
        assert False == True

