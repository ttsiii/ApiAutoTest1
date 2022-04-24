import allure
import pytest
from common.logger import *
from common.logger import Logger
import jsonpath
# @decorate_log
# def assert_api(actual_data,expect_data):
#     # Logger.info("*************** {}开始执行用例 ***************".format(expect_data['info']))
#     try:
#         assert actual_data['code'] == expect_data['except_code']
#         assert actual_data['message'] == expect_data['except_msg']
#     except AssertionError as e:
#         # Logger.error('=====>{}用例执行未通过'.format(expect_data['info']))
#         # 将异常抛出
#         raise e
#     # Logger.info("*************** {}--用例通过 ***************".format(expect_data['info']))

@decorate_log
def assert_api(actual_data,expect_data):
    # Logger.info("*************** {}开始执行用例 ***************".format(expect_data['info']))
    Logger.info("\r\nassert:\r\n 实际结果：{}，\r\n期望结果{}".format(actual_data, expect_data))
    try:
        a = expect_data
        b = actual_data
        for i, j in a.items():
            if i in b.keys():
                assert j == b[i]
        # for i in a.keys():
        #     if i == 'data':
        #         a = a['data']
        #         if i in b.keys():
        #             assert a == b[i]
    except AssertionError as e:
        # Logger.error('=====>{}用例执行未通过'.format(expect_data['info']))
        # 将异常抛出
        raise e
    # Logger.info("*************** {}--用例通过 ***************".format(expect_data['info']))


"""
## 此时用字典来实现的话
a = {"a":1,"b":2}
b = {"a":1,"b":2,"c":3}

### 可知a是b的子集，想要的结果就是a存在与b中时，给我true，不存在给我false


## 如果用字典方法来处理这种情况
for i,j in a.items():
    print(i,j)
    if i in b.keys():
        print(i)
        if j == b[i]:
            print(f"a的值存在与b中,{i,j}")
"""