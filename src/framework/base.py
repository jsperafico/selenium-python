from framework.webdriver import WebDriverWaitContainer, WebDriverContainer
from selenium.webdriver.common.by import By

class BasePageElement(object):
    def __init__(self):
        self.locator:By

    def __set__(self, obj:WebDriverContainer, value):
        driver = obj.instance
        WebDriverWaitContainer(obj).wait.until(lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        element.clear()
        element.send_keys(value)

    
    def __get__(self, obj:WebDriverContainer, owner):
        driver = obj.instance
        WebDriverWaitContainer(obj).wait.until(lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute('value')
    

class BasePage(object):
    def __init__(self, container:WebDriverContainer):
        self.container = container