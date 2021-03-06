# -*- coding:utf-8 -*-
import allure
from api.api_admin import ApiAdmin
from tools.get_token import get_token


@allure.feature("订单查询测试")
class TestAdminOrderSelect(object):
    def setup_class(self):
        # 初始化，实例后台管理类
        self.admin = ApiAdmin()


    @allure.title("查询订单列表成功")
    def test01_order_select(self):
        with allure.step("登录"):
            # 调用登录接口
            r = self.admin.api_login(userName="admin", password="f43fca80ac4e65047a3f011ce47b114633717c06")
            # 获取token
            get_token(r)
        with allure.step("查询订单列表"):
            # 调用订单查询接口
            r = self.admin.api_order_select()
            try:
                # 断言
                assert 'success' == r.json().get("msg")
                print("查找订单列表成功")
            except Exception as e:
                print("查找订单列表失败", e)






