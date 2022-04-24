#作者：道长
import  sys
from api import client
import os
import pytest
import allure

from common.logintoken import *
from common.read_token import read_token

sys.path.append("..")
#对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中。
# 在程序开头加上：
# import sys
# sys.path.append(’引用模块的地址')
# from common.read_yaml import ReadYamlData
# Receiving = ReadYamlData("/admin_data/receiving.yml").get_yaml_data()#读取数据
from common.route import *

class ReceivingApi(client.HttpClient):

    def __init__(self,token):
        # super().__init__()
        self.host = data['admin_host']
        xin_token = read_token(token)
        print("xin_tokenxin_tokenxin_token:",xin_token)
        self.token = xin_token



    """添加收货地址"""
    # data = Receiving['add_shipping_address']['data']
    data0 = add_shipping_address['case_data'][0]['body']
    def add_shipping_address(self
                ,city=data0['city']
                ,detailAddress=data0['detailAddress']
                ,name=data0['name']
                ,phoneNumber=data0['phoneNumber']
                ,postCode=data0['postCode']
                ,province=data0['province']
                ,region=data0['region']
                             ):
        body = {
                "city": city,
                "defaultStatus": 0,
                "detailAddress": detailAddress,
                "id": 0,
                "memberId": 0,
                "name": name,
                "phoneNumber": phoneNumber,
                "postCode": postCode,
                "province": province,
                "region": region
            }
        url = add_shipping_address['url']
        method = add_shipping_address['method']
        url = self.get_full_url(url)
        return self.send(url,body,method=method,x_token=self.token)


    """显示所有收货地址"""
    data0 = address_list['case_data'][0]['body']
    def address_list(self):
        url = address_list['url']
        url = self.get_full_url(url)
        return self.send(url,method="get",x_token=self.token)

    """删除收货地址"""
    # data = Receiving['address_delete']['data']
    data0 = address_delete['case_data'][0]['body']
    def address_delete(self
                ,id=data0['id']):
        url = address_delete['url']
        method = address_delete['method']
        url = self.get_full_url(url,replace=str(id))
        # print("urlurlurlurl",url)
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
    # #
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