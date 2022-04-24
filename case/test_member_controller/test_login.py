import sys
from common.assert_api import assert_api
import allure
import pytest
from common.logger import Logger
sys.path.append("..")
# from common.read_yaml import ReadYamlData
from common.route import *
from common.logger import *
import time


# member_controller = ReadYamlData("duo_data/admin_data/member_controller.yml").get_yaml_data()#读取数据
data =login['case_data']

print('data11:',data)
# # print(data[0][1]['info'])
# for i in range(len(data)):
#     print(data[i][0]['info'])
# #     print("66666",i)
@allure.feature('测试member_controller模块')
@allure.story('登录功能')
# @pytest.mark.smoke
class Test_DengLu():
    @decorate_log
    @pytest.mark.parametrize("case_data", data,ids=[data[i]['case_name'] for i in range(len(data))])  # 参数化测试用例
    def test_admin_login(self,case_data,member_controller_z):
        # time.sleep(10)
        print("case_data",case_data)
        case_body = case_data['body']
        """请求登录测试用例"""
        with allure.step('登录步骤'):
            actual_data = member_controller_z.login(password=case_body['password']
                           ,username=case_body['username'])
            """断言"""
            print("账号密码",case_body['username'],case_body['password'])
            print("哈哈哈哈绝了:",actual_data)
            assert_api(actual_data,case_data['expect'])


if __name__=="__main__":
    pytest.main(['-s',__file__])

