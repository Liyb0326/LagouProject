import json

from selenium1.Page.index import Index
from selenium1.Page.login import Login


class TestLogin:
    def setup(self):
        cookietest = json.load(open(r'F:\PycharmProjects\test\selenium1\Page\cookie.txt', 'r'))
        self.index = Index(reuse=True, cookie_test=cookietest)

    def test_login(self):
        print("登录开始")
        addmen = self.index.go_to_login()
        print("登录成功")
        #跳转新增成员页面
        member = addmen.go_to_member()
        #新增成员
        member.add_member()
        assert member.get_first_member() == "adacd1"
