# -*- coding:utf-8 -*-
import pytest
from api.api_miniprogram import ApiMiniProgram
from tools.read_yaml import read_yaml
import allure


@allure.feature("创建理赔订单测试")
class TestCreateOrder(object):
    # 实例化小程序类对象
    def setup_class(self):
        self.mini = ApiMiniProgram()

    @pytest.mark.skip
    @pytest.mark.parametrize("orderType, claimDes, name, tel", read_yaml("mini_create_order.yaml"))
    def test01_create_order(self, orderType, claimDes, name, tel):
        # 调用创建订单方法,并返回响应对象
        r = self.mini.api_create_order(orderType, claimDes, name, tel)
        # 断言
        try:
            assert "操作成功" == r.json().get("msg")
            print("创建订单成功了！")
        except Exception as e:
            print("创建订单失败", e)




