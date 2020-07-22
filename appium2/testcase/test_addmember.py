from time import sleep

import pytest
import yaml
from pytest import __main__

from appium2.basefunction.app import AppPage


class TestAddMember:
    @classmethod
    def setup_class(cls):
        cls.main = AppPage().start()

    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def teardown_class(self):
        pass

    @pytest.mark.parametrize("username,sex,textmobile", yaml.safe_load(open('../testdata/userinfo.yml', encoding='utf-8')))
    def test_addmenber(self, username, sex, textmobile):
        pagetest = self.main.goto_addressbook().goto_addmenber().goto_contactadd().set_username(username).set_sex(
            sex).set_mobile(textmobile).save_info()
        #pagetest.goback()

    def test_delmenber(self):
        print(self.main)
        sleep(10)


if __name__ == __main__:
    pytest.main(['test_addmember.py'])
