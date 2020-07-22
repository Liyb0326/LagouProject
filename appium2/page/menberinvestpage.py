from selenium.webdriver.common.by import By

from appium2.basefunction.base_page import BasePage


class MenberInvestPage(BasePage):
    def goto_contactadd(self):
        self.find(By.ID, 'com.tencent.wework:id/hgx').click()
        from appium2.page.contactaddpage import ContactAddPage
        return ContactAddPage(self._driver)

    def goback(self):
        self.find(By.ID, 'com.tencent.wework:id/h9e').click()
        from appium2.page.mainpage import MainPage
        return MainPage(self._driver)