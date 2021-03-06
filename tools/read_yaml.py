# -*- coding:utf-8 -*-
import yaml
from config import BASE_PATH
import os


def read_yaml(filename):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(filepath, "r", encoding="utf-8") as f:
        # 定义空列表存储[()]格式数据
        arrs = []
        # 循环遍历，获取参数值
        for data in yaml.safe_load(f).values():
            # 将参数值存储到列表中
            arrs.append(tuple(data.values()))
        return arrs


if __name__ == '__main__':
    print(read_yaml("admin_login.yaml"))





