from selenium.webdriver.common.by import By

from selenium1.Page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        #self.driver.find_element_by_id("username").send_keys("adacd")
        #self.driver.find_element_by_id("memberAdd_acctid").send_keys("adcdefgf")
        #self.driver.find_element_by_id("memberAdd_phone").send_keys("18767122713")
        #self.driver.find_element(By.CSS_SELECTOR, '.js_member_editor_form>div:nth-child(1)>a:nth-child(2)').click()

        self.find(By.ID,"username").send_keys("adacd")
        self.find(By.ID, "memberAdd_acctid").send_keys("adcdefgf")
        self.find(By.ID, "memberAdd_phone").send_keys("18767122713")
        self.find(By.CSS_SELECTOR, '.js_member_editor_form>div:nth-child(1)>a:nth-child(2)').click()

    def get_first_member(self):
        #return self.driver.find_element(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(2)').get_attribute('title')
        return self.find(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(2)').get_attribute('title')
