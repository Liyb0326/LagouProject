from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appium2.basefunction.base_page import BasePage


class ContactAddPage(BasePage):
    def set_username(self, username):
        xm_id = self.find(By.XPATH, "//*[contains(@text,'姓名')]/..//"
                                                   "*[@resource-id='com.tencent.wework:id/awt']")
        xm_id.send_keys(username)
        return self

    def set_sex(self, sex):
        self.find(By.XPATH, "//*[contains(@text,'性别')]/..//*[@resource-id='com.tencent.wework:id/axu']").click()
        if sex == '男':
            self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else:
            self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女")').click()
        return self

    def set_mobile(self, textmobile):
        self.find(By.ID, 'com.tencent.wework:id/f1e').send_keys(textmobile)
        return self

    def save_info(self):
        self.find(By.ID, 'com.tencent.wework:id/h9w').click()
        from appium2.page.menberinvestpage import MenberInvestPage
        return MenberInvestPage(self._driver)
