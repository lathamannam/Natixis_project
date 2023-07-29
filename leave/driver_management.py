import os
from selenium import webdriver
import time


class DriverManager:

    def __init__(self):
        self.driver = None
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.driver_location = "C:\\Users\\pushpalatha\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe"
        self._initialize_driver()

    def _initialize_driver(self):
        if not os.path.exists(self.driver_location):
            raise Exception("Chrome Driver is not present : {}".format(self.driver_location))
        self.driver = webdriver.Chrome(executable_path=self.driver_location)
        self.driver.maximize_window()
        self._launch()

    def _launch(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()



if __name__ == "__main__":
    obj = DriverManager()

