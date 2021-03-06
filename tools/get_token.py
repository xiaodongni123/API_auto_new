# -*- coding:utf-8 -*-
import api

def get_token(response):
    api.admin_headers["cookie"] = "x-auth-token=" + response.cookies["x-auth-token"]