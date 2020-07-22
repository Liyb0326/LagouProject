import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = ""
    base_url = ""

    def __init__(self, reuse=False, cookie_test=[]):
        if reuse == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=opts)
            self._driver.implicitly_wait(3)
            if len(cookie_test) > 0:
                self._driver.get('https://work.weixin.qq.com/')
                for cookie in cookie_test:
                    self._driver.add_cookie(cookie)
        else:
            self._driver = webdriver.Chrome()

        if self.base_url != "":
            self._driver.get(self.base_url)

    def get_cookies(self):
        cookies = self._driver.get_cookies()
        with open('cookie.txt', 'w') as f:
            json.dump(cookies, f)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def wait_for(self, fun):
        WebDriverWait(self._driver, 10).until(fun)


if __name__ == '__main__':
    BasePage(reuse=True).get_cookies()

