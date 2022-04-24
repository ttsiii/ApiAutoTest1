import os
import configparser
from common.route import *


def read_token(token):
    conf_file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/configs/token.ini")  # 保存文件路径
    config = configparser.ConfigParser()
    config.read(conf_file, encoding='utf-8')
    xin_token = config.get("token", "{}".format(token))
    return xin_token

# """登录3333"""
# data0 = login['case_data'][0]['body']
# print('data0111111111',data0)
# def login1(password=data0['password'],username=data0['username']):
#     etc = {
#             "password": password,
#             "username": username
#             }
#     url = login['url']
#     method = login['method']
#     url = self.get_full_url(url,etc=etc)
#     return self.send(url,method=method)

if __name__ == '__main__':
    read_token('zhangsan_token')