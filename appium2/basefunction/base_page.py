from typing import List

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    _black_list = {
        (MobileBy.XPATH, '//*[@text="确定"]'),
        (MobileBy.XPATH, '//*[@text="允许"]')
    }
    _err_num = 0
    _max_num = 5

    def __init__(self, driver: webdriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            #return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            print(locator)
            if isinstance(locator, tuple):
                return self._driver.find_element(*locator)
            else:
                print(locator)
                return self._driver.find_element(locator, value)
        except Exception as e:
            if self._err_num > self._max_num:
                raise e
            else:
                self._err_num += 1
                for ele in self._black_list:
                    elemnts = self._driver.find_elements(*ele)
                    if len(elemnts) > 0:
                        elemnts[0].click()
                        self.find(locator, value)
            raise e

    def steps(self, fpath, name):
        with open(fpath, 'r', encoding='utf-8') as f:
            listact: List[dict] = yaml.safe_load(f)
            print(listact)
            print(name)
            for list in listact:
                print(list)
                if name == list['name']:
                    print(name)
                    print(list['name'])
                    if 'By' in list.keys():
                        myby = list['By']
                        if myby == 'xpath':
                            elemt = self.find(MobileBy.XPATH, list['locator'])
                        if myby == 'id':
                            elemt = self.find(MobileBy.XPATH, list['locator'])
                        if myby == 'android_uiautomator':
                            print('滚动查找')
                            elemt = self.find(MobileBy.ANDROID_UIAUTOMATOR, list['locator'])
                    if 'action' in list.keys():
                            elemt.click()
                else:
                    print("没有需要处理的步骤")
                    continue
