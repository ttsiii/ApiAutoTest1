#作者：道长
import  sys
import requests
from until.phone import TestFaker
from common.logintoken import *
from api import client
from common.readCofig import Environ
from common.logintoken import *
from common.read_token import read_token
sys.path.append("..")
#对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中。
# 在程序开头加上：
# import sys
# sys.path.append(’引用模块的地址')
from common.read_yaml import get_yaml_filepath
# data = ReadYamlConfigs("data.yaml").get_yaml_data()#读取数据
data = get_yaml_filepath(Environ=Environ)

# member_controller = ReadYamlData("/admin_data/member_controller.yml").get_yaml_data()#读取数据
from common.route import *

class MemberControllerApi(client.HttpClient):

    def __init__(self,token):
        # super().__init__()
        self.host = data['admin_host']
        xin_token = read_token(token)
        self.token = xin_token

    """-------------------------------商城前台--------------------------------------------------"""
    """获取注册验证码"""
    # data = member_controller['get_auth_code']['data'][0]
    data0 = get_auth_code['case_data'][0]['body']
    def get_auth_code(self,telephone = TestFaker().get_phone_number()):
        # print("TestFaker().get_phone_number()",telephone)
        etc = {
                "telephone": telephone
                }
        url = get_auth_code['url']
        method = get_auth_code['method']
        url = self.get_full_url(url,etc=etc)
        return self.send(url, method=method)

    """注册"""
    # data = member_controller['register']['data'][0]
    data0 = register['case_data'][0]['body']
    def register(self
                       ,authCode=data0['authCode']
                       ,password=data0['password']
                       ,telephone=data0['telephone']
                       ,username=data0['username']):
        etc = {
                "authCode": authCode,
                "password": password,
                "telephone": telephone,
                "username": username
                }
        url = register['url']
        method = register['method']
        url = self.get_full_url(url,etc=etc)
        return self.send(url, method=method)

    """登录接口封装"""
    # data0 = login['case_data'][0]['body']
    def login(self,username,password):
        return login1(username,password)

    """获取会员信息"""
    def getmember_info(self):
        url = member_controller['getmember_info']['url']
        method = member_controller['getmember_info']['method']
        url = self.get_full_url(url)
        return self.send(url,method=method,x_token=self.token)


    # "总后台-登录"
    # data = login_data['login_admin']['data']
    # def admin_login0(self,account=data['account'],password=data['password']):
    #     body = {
    #             "account": account,
    #             "password": password
    #             }
    #     data = login_data['login_admin']
    #     url = self.get_full_url(data['url'])
    #     print("url",url)
    #     print("body",body)
    #     return self.send(url,body,method=data['method'])
    #
    # "总后台-新增课程"
    # data = course_data['add_course']['data']
    # def admin_add_kecheng(self,token,coverKey=data['coverKey']
    #                       ,mode = data['mode']
    #                       ,name = data['name']
    #                       ,teacher = data['teacher']
    #                       ,subject = data['subject']
    #                       ,type = data['type']):
    #     body = {
    #             "coverKey": coverKey,
    #             "mode": mode,
    #             "name": name,
    #             "subject": subject,
    #             "teacher": teacher,
    #             "type": type}
    #     data = course_data['add_course']
    #     url = self.get_full_url(data['url'])
    #     return self.send(url,body,method=data['method'],x_token=token)
    # "总后台-上架课程"
    # data = course_data['shelve_course']['data']
    # def admin_shelve_course(self,token,courseId=data['courseId']):
    #     body = {
    #             "courseId": courseId}
    #     data = course_data['shelve_course']
    #     url = self.get_full_url(data['url'])
    #     return self.send(url,body,method=data['method'],x_token=token)
    #
    # "总后台-下架课程"
    # data = course_data['unshelve_course']['data']
    # def admin_unshelve_course(self,token,courseId=data['courseId']):
    #     body = {
    #             "courseId": courseId}
    #     data = course_data['unshelve_course']
    #     url = self.get_full_url(data['url'])
    #     return self.send(url,body,method=data['method'],x_token=token)
    #
    # """-------------------------------iShow-admin 结尾--------------------------------------------------"""
    #
    # # 下面是etc和replace用法举例，不过没进行yaml数据替换，不过都一样
    # def admin_get_draw_order(self,ader_id,status,session):
    #     etc = {
    #         "start":0,
    #         "limit":10,
    #         "otc_ader_id":ader_id,
    #         "otc_ader_withdraw_status":status
    #     }
    #     url =self.get_full_url(self.http_map['draw_list'],etc= etc)
    #     return self.send(url,x_token=session)
    #
    # def admin_update_draw_status(self,id,otc_ader_id,status,session):
    #     body = {
    #         "otc_ader_withdraw_status":status,
    #         "otc_ader_id":otc_ader_id
    #     }
    #     url = self.get_full_url(self.http_map['update_draw_status'],replace={id})
    #     return self.send(url,body,method="patch",x_token=session)
    #
    # def admin_get_merchant_info(self,login_name,session):
    #     etc = {
    #         "start":0,
    #         "limit":999,
    #         "merchant_loginname":login_name
    #     }
    #     url = self.get_full_url(self.http_map['get_merchant_info'],etc=etc)
    #     return self.send(url,x_token=session)
    #
    # def admin_get_transac_list(self,session,order_number = ""):
    #     etc = {
    #         "order_number":order_number
    #     }
    #     url = self.get_full_url(self.http_map['get_recharge_transac_list'],etc=etc)
    #     return self.send(url,x_token=session)
    #
    # def admin_get_withdraw_transac_list(self,session,order_number = ""):
    #     etc = {
    #         "order_number": order_number
    #     }
    #     url = self.get_full_url(self.http_map['get_withdraw_transac_list'], etc=etc)
    #     return self.send(url, x_token=session)
    #
    #
    #
    # def admin_duanxin_yzm(self,mobile,session):
    #     etc = {
    #             "nojson": "true",
    #             "mobile": mobile,
    #             "page": 1
    #             }
    #     url = self.get_full_url(self.http_map['admin_duanxin_yzm'], etc=etc)
    #     return self.send(url, x_token=session)