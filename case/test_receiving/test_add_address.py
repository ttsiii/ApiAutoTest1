import sys

import allure
import pytest

from common.assert_api import assert_api
from common.logger import *
sys.path.append("..")
# from common.read_yaml import ReadYamlData
from common.route import *
import time
# receiving = ReadYamlData("duo_data/admin_data/receiving.yml").get_yaml_data()#读取数据
data =add_shipping_address['case_data']


@allure.feature('测试receiving模块')
@allure.story('添加收货地址功能')
class Test_DengLu():


    @allure.title("添加收货地址")
    @allure.step('添加收货地址-显示所有收货地址-删除收货地址')#测试报告显示步骤
    @pytest.mark.usefixtures("del_address")
    @pytest.mark.parametrize("case_data", data,ids=[data[i]['case_name'] for i in range(len(data))])  # 参数化测试用例
    @decorate_log
    def test_admin_login(self,case_data, receiving_l):
        # time.sleep(3)
        case_body = case_data['body']
        """请求添加收货地址"""
        actual_data = receiving_l.add_shipping_address(city=case_body['city']
                ,detailAddress=case_body['detailAddress']
                ,name=case_body['name']
                ,phoneNumber=case_body['phoneNumber']
                ,postCode=case_body['postCode']
                ,province=case_body['province']
                ,region=case_body['region'])
        """断言"""
        assert_api(actual_data,case_data['expect'])





        # assert_api(actual_code=add_shipping_address['code'],expect_code=data['except_code']
        #            ,actual_data=add_shipping_address['message'],expect_data=data['except_msg']
        #            ,doc=data['info'])







if __name__=="__main__":
    pytest.main(['-s',__file__])