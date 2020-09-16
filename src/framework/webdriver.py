try:
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.support.ui import WebDriverWait
except Exception as e:
    print('Some modules are missing {}'.format(e))

class WebDriverContainer(object):
    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://selenium-hub:4444', desired_capabilities=DesiredCapabilities.CHROME)
    
    def quit(self):
        self.driver.quit()
    
    @property
    def instance(self):
        return self.driver

class WebDriverWaitContainer(object):
    def __init__(self, container:WebDriverContainer):
        self.driver = container.instance

    @property
    def wait(self):
        return WebDriverWait(self.driver, 60)
