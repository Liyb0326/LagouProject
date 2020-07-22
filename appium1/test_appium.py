import yaml
from appium import webdriver
from time import sleep
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.common.by import By


class TestClick:
    @classmethod
    def setup_class(self):
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

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(20)
        self.driver.implicitly_wait(6)

    @classmethod
    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        pass
    def teardown(self):
        pass
        # self.driver.find_element(By.ID,'com.tencent.wework:id/h9e').click()

    @pytest.mark.parametrize("username, sex, textmobile", yaml.safe_load(open('./userinfo.yml', "r", encoding='UTF-8')))
    def test_addmember(self, username, sex, textmobile):

        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]').click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                               'new UiSelector().scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector().text("添加成员")'
                                                               '.instance(0));').click()

        assert '.friends.controller.MemberInviteMenuActivity' in self.driver.current_activity

        self.driver.find_element_by_id('com.tencent.wework:id/hgx').click()

        assert ".contact.controller.ContactAddActivity" in self.driver.current_activity

        xm_id = self.driver.find_element(By.XPATH, "//*[contains(@text,'姓名')]/..//"
                                                   "*[@resource-id='com.tencent.wework:id/awt']")
        xm_id.send_keys(username)

        self.driver.find_element(By.XPATH, "//*[contains(@text,'性别')]/..//*[@resource-id='com.tencent.wework:id/axu']").click()
        if sex == '男':
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()

        self.driver.find_element_by_id('com.tencent.wework:id/f1e').send_keys(textmobile)

        self.driver.find_element_by_id('com.tencent.wework:id/h9w').click()
        sleep(2)

    def test_delmember(self):
        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]').click()
        sleep(3)
        self.driver.find_element(By.ID, 'com.tencent.wework:id/h9u').click()
        while True:
            list_elements = self.driver.find_elements(By.XPATH, "//*[@resource-id='com.tencent.wework:id/hfg']"
                                                                "//*[contains(@text,'测试')]")
            if len(list_elements) > 0:
                text_name = list_elements[0].text
                list_elements[0].click()
                self.driver.find_element_by_id('com.tencent.wework:id/e3f').click()
                self.driver.find_element_by_id('com.tencent.wework:id/bci').click()
                sleep(8)
                print(text_name)
                print(self.driver.page_source)
                assert text_name not in self.driver.page_source
            else:
                print('没有要删除的成员')
                break
