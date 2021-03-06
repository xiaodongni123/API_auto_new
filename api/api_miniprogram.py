# -*- coding:utf-8 -*-
import requests
import api

# 封装小程序接口
class ApiMiniProgram(object):
    # 初始化url
    def __init__(self):
        # 创建订单url
        self.create_order_url = api.mini_url + "/order/save"

    # 构造创建订单
    def api_create_order(self, orderType, claimDes, name, tel):
        """创建订单接口
        :param orderType: 订单类型
        :param claimDes: 描述
        :param name: 名称
        :param tel: 电话
        :param order_mount: 订单金额
        :return: 响应对象
        """
        data = {"orderType": orderType,
                "claimDes": claimDes,
                "name": name,
                "tel": tel,
                "order_mount": 0}
        # 发送post请求，返回响应对象
        return requests.post(url=self.create_order_url, json=data, headers=api.mini_headers)





