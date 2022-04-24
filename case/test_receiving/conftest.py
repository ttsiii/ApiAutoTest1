# # -*- coding: UTF-8 -*-




"""sql举例"""

# from api import app_api
import pytest
# import  sys
# sys.path.append("..")
# from common.db import *
# from action import action_admin,action_saas
# from common.read_yaml import ReadYaml
# data = ReadYaml("data.yaml").get_yaml_data()#读取数据
#
# # -----------------------------操作数据清理--------------------------------------------
#
# 删除课程
# @pytest.fixture(scope="function",autouse=True)
# def del_course():
#     delete_sql('course', 'name','道长课程')
#     yield
#     delete_sql('course', 'name','道长课程')
# #查询课程ID
# @pytest.fixture(scope="session")
# def check_course():
#     return check_sql('id', 'course', 'name', '道长课程')


#数据清理--删除收货地址
@pytest.fixture()
def del_address(receiving_l):
    yield
    """显示所有收货地址"""
    address_list = receiving_l.address_list()
    print("ggggggggggggg",address_list)
    id = address_list['data'][0]['id']
    """删除收货地址"""
    address_delete = receiving_l.address_delete(id=id)