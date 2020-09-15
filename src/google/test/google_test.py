import unittest
from framework.webdriver import WebDriverContainer, WebDriverWaitContainer
from google.pages import GoogleHomePage

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.container = WebDriverContainer()
        self.addCleanup(self.container.quit)
        self.container.driver.get('http://www.google.com')
        self.container.driver.maximize_window()
    
    def testPageTitle(self):
        self.assertIn('Google', self.container.driver.title)
    
    def testIfLogoIsShowing(self):
        home = GoogleHomePage(self.container)
        home.acceptDataUsage()

        value = home.logo.get_attribute('src')
        self.assertIn('/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', value)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)