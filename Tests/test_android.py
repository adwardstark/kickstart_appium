import unittest
from appium import webdriver

class LoginTests(unittest.TestCase):

    def setUp(self):
        app = ('./Test_Android/app/build/outputs/apk/debug/app-debug.apk')
        self.wd = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '9',
                'deviceName': 'Pixel_2_API_28'
            }
        )
    
    def tearDown(self):
        self.wd.quit()
    
    def test_success(self):
        basepath = "//android.widget.LinearLayout[1]/"
        self.wd.find_element_by_xpath(basepath + "android.widget.EditText[1]").send_keys("test@login.com")
        self.wd.find_element_by_xpath(basepath + "android.widget.EditText[2]").send_keys("password")
        self.wd.find_element_by_xpath(basepath + "android.widget.Button[1]").click()
        try:
          self.wd.find_element_by_xpath(basepath + "android.widget.TextView[1]")
        except: 
          self.fail("Not at Login Success page.\n")

    def test_fail(self):
        basepath = "//android.widget.LinearLayout[1]/"
        self.wd.find_element_by_xpath(basepath + "android.widget.EditText[1]").send_keys("test@login.com")
        self.wd.find_element_by_xpath(basepath + "android.widget.EditText[2]").send_keys("wrongpassword")
        self.wd.find_element_by_xpath(basepath + "android.widget.Button[1]").click()
        try:
          self.wd.find_element_by_xpath(basepath + "android.widget.Button[1]")
        except:
          self.fail("Not at Login Success page.\n")
    
    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
        unittest.TextTestRunner(verbosity=2).run(suite)