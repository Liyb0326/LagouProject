from selenium.webdriver.common.by import By

from selenium1.Page.add_member import AddMember
from selenium1.Page.base_page import BasePage


class Login(BasePage):
    def go_to_member(self):
        #self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap').click()
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap').click()
        return AddMember(reuse=True)
