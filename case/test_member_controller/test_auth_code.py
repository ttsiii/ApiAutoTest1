import sys
from common.assert_api import assert_api
import allure
import pytest
# from common.logger import Logger
sys.path.append("..")
# from common.read_yaml import ReadYamlConfigs, ReadYamlData
from common.route import *
from common.logger import *
import time
# member_controller = ReadYamlData("duo_data/admin_data/member_controller.yml").get_yaml_data()#读取数据
# data =member_controller['get_auth_code']['data']
data =get_auth_code['case_data']

@allure.feature('测试member_controller模块')
@allure.story('获取验证码功能')

class TestGetAuthCode():
    @allure.step('随机手机号-获取验证码')#测试报告显示步骤
    @pytest.mark.parametrize("case_data", data,
                             ids=[data[i]['case_name'] for i in range(len(data))])  # 参数化测试用例
    @decorate_log
    def test_get_auth_code(self,case_data, member_controller_z):
        # time.sleep(3)
        case_body = case_data['body']
        actual_data = member_controller_z.get_auth_code(telephone = case_body['telephone'])
        """断言"""
        print("566666:", actual_data)
        # assert_api(actual_data,case_data['expect'])



if __name__=="__main__":
    pytest.main(['-s',__file__])