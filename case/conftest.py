#作者：道长
from common.logger import *
import pytest
import  sys
sys.path.append("..")
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


#
# """-------------------进行初始化登录----------------------"""
# @pytest.fixture(scope="session",autouse=True)
# def azs_login(zhangsan_info):
#     login_zs(zhangsan_info,'zhangsan_token')
# # def test_zhansgan_login(zhangsan_login):
# #     print("张三登录")
#
# @pytest.fixture(scope="session",autouse=True)
# def als_login(lisi_info):
#     login_ls(lisi_info,'lisi_token')
# # def test_lisi_login(lisi_login):
# #     print("李四登录")
#
#
# """----------------获取账号数据----------------------------"""
# @pytest.fixture(scope="session")
# def zhangsan_info():
#     return data['zhangsan']
#
# @pytest.fixture(scope="session")
# def lisi_info():
#     return data['lisi']
# """-----------------调用api并且进行token身份切换-----------------"""
#
# """张三模块"""
# @pytest.fixture(scope="session")
# def member_controller_z():
#     return MemberControllerApi("zhangsan_token")
#
# @pytest.fixture(scope="session")
# def receiving_z():
#     return ReceivingApi("zhangsan_token")
#
# """李四模块"""
# @pytest.fixture(scope="session")
# def member_controller_l():
#     return MemberControllerApi("lisi_token")
#
# @pytest.fixture(scope="session")
# def receiving_l():
#     return ReceivingApi("lisi_token")
#
#
#


"""--------------------------------------------------动态传参到下个接口封装-----------------------------------------------"""
@pytest.fixture(scope="session")
def yzm(member_controller_l,member_controller_z):
    """获取验证码"""
    phone = TestFaker().get_phone_number()
    get_auth_code_l = member_controller_l.get_auth_code(telephone=phone)
    get_auth_code_z = member_controller_z.get_auth_code(telephone=phone)
    yzm_l = get_auth_code_z['data']
    yzm_z = get_auth_code_z['data']
    return phone,yzm_l,yzm_z


# conftest.py

import time
from _pytest import terminal



def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    print("===============pytest_terminal_summary===================")
    print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len(terminalreporter.stats.get('passed', [])))
    print('failed:', len(terminalreporter.stats.get('failed', [])))
    print('error:', len(terminalreporter.stats.get('error', [])))
    print('skipped:', len(terminalreporter.stats.get('skipped', [])))
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 'seconds')

# # 添加命令行参数
# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdhost",
#         action="store",
#         # default: 默认值，命令行没有指定host时，默认用该参数值
#         default="http://www.baidu.com",
#         help="获取当前代码执行环境"
#     )
#
# # autouse=True自动执行该前置操作
# @pytest.fixture(scope="session", autouse=True)
# def host(request):
#     '''获取命令行参数'''
#     # 获取命令行参数给到环境变量
#     os.environ["host"] = request.config.getoption("--cmdhost")
#     print("当前用例运行测试环境:%s"%os.environ["host"])
#     return os.environ["host"]
