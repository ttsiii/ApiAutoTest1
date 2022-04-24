import sys
from common.assert_api import assert_api
import allure
import pytest
from common.logger import Logger
sys.path.append("..")
from until.phone import TestFaker
# from common.read_yaml import ReadYamlConfigs, ReadYamlData
from common.route import *
import time

# data =member_controller['register']['data']
data =register['case_data']
@allure.feature('测试member_controller模块')

# @allure.story('注册功能')
class Test_DengLu():

    @allure.title("正常注册999")
    @allure.step('随机手机号-注册')#测试报告显示步骤
    @pytest.mark.parametrize("case_data", data,ids=[data[i]['case_name'] for i in range(len(data))])  # 参数化测试用例
    def test_register(self,case_data, yzm,member_controller_l):

        # """获取验证码"""
        # phone = TestFaker().get_phone_number()
        # get_auth_code = membercontroller_l.get_auth_code(telephone=phone)
        # yzm = get_auth_code['data']
        "注册"
        actual_data = member_controller_l.register(authCode=yzm[1],telephone=yzm[0],username="admin"+yzm[0])
        case_body = case_data['body']
        """断言"""
        assert_api(actual_data,case_data['expect'])


if __name__=="__main__":
    pytest.main(['-m smoke',__file__])