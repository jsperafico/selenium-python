try:
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.by import By
    from selenium.webdriver import Remote
    from src.framework.base import BasePage 
    from src.framework.webdriver import WebDriverWaitContainer, WebDriverContainer
except Exception as e:
    print('Some modules are missing {}'.format(e))

class GoogleHomePage(BasePage):

    def __init__(self, container:WebDriverContainer):
        BasePage.__init__(self, container)

    def acceptDataUsage(self):
        WebDriverWaitContainer(self.container).wait.until(ec.frame_to_be_available_and_switch_to_it(GoogleHomeLocators.DATA_USAGE_DIALOG))
        self.container.instance.find_element(*GoogleHomeLocators.ACCEPT_DATA_USAGE).click()

        WebDriverWaitContainer(self.container).wait.until(ec.invisibility_of_element(GoogleHomeLocators.DATA_USAGE_DIALOG))
        self.container.instance.switch_to.default_content()
    
    @property
    def logo(self):
        WebDriverWaitContainer(self.container).wait.until(ec.visibility_of_element_located(GoogleHomeLocators.LOGO))
        element = self.container.instance.find_element(*GoogleHomeLocators.LOGO)
        return element

class GoogleHomeLocators(object):
    LOGO = (By.CSS_SELECTOR, '#body img')
    DATA_USAGE_DIALOG = (By.CSS_SELECTOR, 'div[role="dialog"] iframe')
    ACCEPT_DATA_USAGE = (By.CSS_SELECTOR, '#introAgreeButton')