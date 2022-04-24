import configparser

import yaml

from api import client
import os
import pytest
import allure
#对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中。
# 在程序开头加上：
# import sys
# sys.path.append(’引用模块的地址')
from common.read_yaml import get_yaml_filepath
from common.readCofig import Environ

# data = ReadYamlConfigs("data.yaml").get_yaml_data()#读取数据
data = get_yaml_filepath(Environ=Environ)
from common.route import *


from api.client import HttpClient
clent1 = HttpClient()
data0 = login['case_data'][0]['body']


# print("1121",data0)
def login1(username=data0['username']
          , password=data0['password']):
    etc = {
        "username": username
        , "password": password
    }

    url = login['url']
    method = login['method']
    url = clent1.get_full_url(url, etc=etc)
    return clent1.send(url, method=method)

class Login(client.HttpClient):

    def __init__(self, admin_info,token):
        super().__init__()
        self.username = admin_info['user_name']
        self.password = admin_info['password']
        result = login1(username=self.username, password=self.password)
        # assert result['code'] == 200,"前台登录失败"
        self.token = result['data']['token']
        # 把token值写入配置文件中
        self.conf_file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/configs/token.ini")# 保存文件路径
        config = configparser.ConfigParser()

        # 打开配置文件
        config.read(self.conf_file, encoding='utf-8')
        # 在配置文件中设置token的值
        # config.set("token", "zhangsan_token", str(self.token))
        config.set("token", "{}".format(token), str(self.token))
        config.write(open(self.conf_file, "w"))  # w+ ：修改配置文件的内容并保存

    # @allure.step("admin账号登录")
    # def admin_login(self):
    #     return self.login(username=self.username, password=self.password)

    # """登录3333"""
    # data0 = login['case_data'][0]['body']
    # print('data0111111111',data0)
    # def login(self
    #                    ,password=data0['password']
    #                    ,username=data0['username']):
    #     etc = {
    #             "password": password,
    #             "username": username
    #             }
    #     url = login['url']
    #     method = login['method']
    #     url = self.get_full_url(url,etc=etc)
    #     return self.send(url,method=method)

def login_zs(admin_info,zs_token):
    return Login(admin_info,zs_token)

def login_ls(admin_info,ls_token):
    return Login(admin_info,ls_token)


# class LiSiLogin(client.HttpClient):
#
#     def __init__(self, admin_info):
#         super().__init__()
#         self.host = data['admin_host']
#
#         self.username = admin_info['user_name']
#         self.password = admin_info['password']
#         result = self.admin_login()
#         print("result:",result)
#         assert result['status_code'] == 200,"前台登录失败"
#         self.token = result['data']['data']['token']
#         # print("token2222222222222222222222222:",self.token)
#         # 把token值写入配置文件中
#         self.conf_file = r'D:\daima\pytest-automation-huice\configs\token.ini'  # 保存文件路径
#         config = configparser.ConfigParser()
#
#         # 打开配置文件
#         config.read(self.conf_file, encoding='utf-8')
#         # 在配置文件中设置token的值
#         config.set("token", "lisi_token", str(self.token))
#         config.write(open(self.conf_file, "r+"))  # r+ ：修改配置文件的内容并保存
#
#     @allure.step("总后台账号登录")
#     def admin_login(self):
#         return self.login(username=self.username, password=self.password)
#
#     """登录"""
#     data = MemberController['login']['data']
#     def login(self
#                        ,password=data['password']
#                        ,username=data['username']):
#         etc = {
#                 "password": password,
#                 "username": username
#                 }
#         url = MemberController['login']['url']
#         url = self.get_full_url(url,etc=etc)
#         return self.send(url,method="post")
