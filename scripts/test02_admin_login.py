# -*- coding:utf-8 -*-
from api.api_admin import ApiAdmin
import pytest
from tools.read_yaml import read_yaml
import allure


# 创建测试登录接口类
@allure.feature("后台管理系统登录测试")
class TestAdminLogin(object):
    def setup_class(self):
        # 初始化，获取登录接口对象
        self.admin = ApiAdmin()

    @allure.story("登录")
    @pytest.mark.parametrize("title, userName, password, expect_reslut", read_yaml("admin_login.yaml"))
    def test01_login(self,title, userName, password, expect_reslut):
        allure.dynamic.title(title)
        # 调用登录接口，返回响应对象
        r = self.admin.api_login(userName, password)
        try:
            # 断言
            assert expect_reslut == r.json().get("msg")
            print("登录成功")
        except Exception as e:
            print("登录失败", e)




