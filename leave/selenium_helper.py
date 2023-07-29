from selenium.webdriver.support.ui import Select

class SeleniumHelper:

    def __init__(self, driver):
        self.driver = driver


    def identify_element(self, locator_value, locator_type, element_name):
        try:
            if locator_type == "ID":
                element = self.driver.find_element_by_id(locator_value)
            elif locator_type == "XPATH":
                element = self.driver.find_element_by_xpath(locator_value)
            return element
        except Exception as e:
            print("Unable to find the element :{} ERROR: {}".format(element_name, str(e)))

    def click(self, element):
        try:
            element.click()
        except Exception as e:
            print("Unable to click the element")

    def send_text(self, elem, text):
        try:
            elem.send_keys(text)
        except Exception as e:
            print("Unable to enter a text")

    def selecting_element(self,elem, visible_text):
        try:

            drop = (Select(elem)).select_by_visible_text(visible_text)
            return drop
        except Exception as e:
            print("Unable to find the text :{} ERROR: {}".format(visible_text, str(e)))

    def identifying_elements(self, locator_type, locator_value, element_name):
        try:
            if locator_type == 'ID':
                actual_date = self.driver.find_elements_by_id(locator_value)
            elif locator_type == 'XPATH':
                actual_date = self.driver.find_elements_by_xpath(locator_value)
                return actual_date
        except Exception as e:
            print("Unable to find the elements :{} ERROR: {}".format(element_name, str(e)))

    def calendar_from_date(self,actual_date,select_date):
        try:
            for dates in actual_date:
                date = dates.text
                if date == select_date:
                    dates.click()
                    break
        except Exception as e:
            print("Unable to find the element :{} ERROR: {}".format(select_date, str(e)))


    def calendar_to_date(self,actual_date,select_date):
        try:
            for dates in actual_date:
                date = dates.text
                if date == select_date:
                    dates.click()
                    break
        except Exception as e:
            print("Unable to find the element :{} ERROR: {}".format(select_date, str(e)))

    def clear_test(self, element):
        try:
            element.clear()
        except Exception as e:
            print("unable to clear the text")

