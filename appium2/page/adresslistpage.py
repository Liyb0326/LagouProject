from appium2.basefunction.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from time import sleep




class AdressListPage(BasePage):
    def goto_addmenber(self):
        """
                self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                 'new UiSelector().scrollable(true).instance(0))'
                                                 '.scrollIntoView(new UiSelector().text("添加成员")'
                                                 '.instance(0));').click()
        :return:
        """

        self.steps('../pagesteps/addmenber.yml', 'gotoaddmenber')
        sleep(5)
        from appium2.page.menberinvestpage import MenberInvestPage
        return MenberInvestPage(self._driver)
