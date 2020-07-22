from time import sleep

from appium2.basefunction.base_page import BasePage
from appium import webdriver

from appium2.page.mainpage import MainPage


class AppPage(BasePage):
    def start(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnAet'] = 'true'
        desired_caps['automationName'] = 'UiAutomator1'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'

        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(20)
        self._driver.implicitly_wait(6)
        return MainPage(self._driver)

    def stop(self):
        self._driver.quit()
