# -*- coding:utf-8 -*-
import requests
import api


# 创建后台管理系统api类
class ApiAdmin(object):
    def __init__(self):
        # 登录url
        self.login_url = api.admin_url + "/sys/login"
        # 订单查询url
        self.order_select_url = api.admin_url + "/order/findByPage"

    # 封装登录接口方法
    def api_login(self, userName, password):
        # 请求体
        data = {"userName": userName,
                "password": password,
                "type": "account"}
        # 调用post方法，返回响应对象
        return requests.post(url=self.login_url, json=data, headers=api.admin_headers)

    # 封装订单查询接口方法
    def api_order_select(self):
        # 调用get方法，返回响应对象
        return requests.get(url=self.order_select_url, headers=api.admin_headers)


