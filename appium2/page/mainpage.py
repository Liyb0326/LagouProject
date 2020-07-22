from selenium.webdriver.common.by import By

from appium2.basefunction.base_page import BasePage



class MainPage(BasePage):
    def goto_addressbook(self):
        #self.find(By.XPATH, '//*[@text="通讯录"]').click()
        self.steps('../pagesteps/addmenber.yml', 'gotoaddressbook')
        from appium2.page.adresslistpage import AdressListPage
        return AdressListPage(self._driver)
