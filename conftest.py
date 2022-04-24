#作者：道长
from common.logger import *
import pytest
import  sys
# sys.path.append("..")
from common.db import *
from common.assert_api import assert_api
from common.read_yaml import get_yaml_filepath
from common.logintoken import login_zs,login_ls
from api.admin.member_controller_api import MemberControllerApi
from api.admin.receiving_api import ReceivingApi
from common.readCofig import zhangsan_token,lisi_token
from common.readCofig import Environ
from until.phone import TestFaker

# data = ReadYamlConfigs("data.yaml").get_yaml_data()#读取数据
data = get_yaml_filepath(Environ=Environ)



"""-------------------进行初始化登录----------------------"""
@pytest.fixture(scope="session",autouse=True)
def azs_login(zhangsan_info):
    login_zs(zhangsan_info,'zhangsan_token')
# def test_zhansgan_login(zhangsan_login):
#     print("张三登录")

@pytest.fixture(scope="session",autouse=True)
def als_login(lisi_info):
    login_ls(lisi_info,'lisi_token')
# def test_lisi_login(lisi_login):
#     print("李四登录")


"""----------------获取账号数据----------------------------"""
@pytest.fixture(scope="session")
def zhangsan_info():
    return data['zhangsan']

@pytest.fixture(scope="session")
def lisi_info():
    return data['lisi']
"""-----------------调用api并且进行token身份切换-----------------"""

"""张三模块"""
@pytest.fixture(scope="session")
def member_controller_z():
    return MemberControllerApi("zhangsan_token")

@pytest.fixture(scope="session")
def receiving_z():
    return ReceivingApi("zhangsan_token")

"""李四模块"""
@pytest.fixture(scope="session")
def member_controller_l():
    return MemberControllerApi("lisi_token")

@pytest.fixture(scope="session")
def receiving_l():
    return ReceivingApi("lisi_token")



