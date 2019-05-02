import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

    def setUp(self):
        app = ('./Test_iOS/build/Release-iphonesimulator/TestAppiumApp.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.2',
                'deviceName': 'iPhone 8'
            }
        )
    
    def tearDown(self):
        self.driver.quit()

    def test_success(self):
        emailTF = self.driver.find_element_by_accessibility_id('txtEmail')
        emailTF.send_keys("test@login.com")
        emailTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertEqual(emailTF.get_attribute("value"), "test@login.com")

    def test_fail(self):
        passwordTF = self.driver.find_element_by_accessibility_id('txtPassword')
        passwordTF.send_keys("validPW")
        passwordTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertNotEqual(passwordTF.get_attribute("value"), "validPW")

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
        unittest.TextTestRunner(verbosity=2).run(suite)