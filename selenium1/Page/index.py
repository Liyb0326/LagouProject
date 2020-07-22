from selenium1.Page.base_page import BasePage
from time import sleep

from selenium1.Page.login import Login


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def go_to_register(self):
        pass

    def go_to_login(self):
        print("地址跳转")
        #self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        return Login(reuse=True)

