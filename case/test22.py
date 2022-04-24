# var = {}
# if var:
#     print('Not Null')
# else:
# #     print('Is Null')
# from urllib import parse
# daozhang = {
#     "code": "0",
#     "message": "成功!",
#     "data": "https://pay.medbanks-test.cn/#/?orderCacheId=1495949324251951104&saleChannelId=d645920e395fedad&skuCode=200003549&uuid=5d9cb0b4-cbc2-482e-b918-8203e37b90f4",
#     "errorClass": None,
#     "errorStack": None,
#     "violationItems": None,
#     "success": True,
#     "failure": False,
#     "error": False
# }
# url = daozhang["data"].replace('#','')
# print(url)
# test = parse.parse_qs(parse.urlparse(url).query)
# print(test)
# print(test['orderCacheId'][0])
#
#
# dict={'log_id': 5891599090191187877, 'result_num': 1, 'result': [{'probability': 0.9882395267486572, 'top': 205,
# 'height': 216, 'classname': 'Face', 'width': 191, 'left': 210}]}
# # 1.访问dict的值
#
# print(dict['log_id'])
# # 2.访问dict下的result列表的值：
#
# print(dict['result'][0]['top'] )# dict下的result列表的第一个值（字典）的top内容
# # 　3.也可以使用临时变量:
#
# dict1=dict['result']
# print(dict1[0]['probability'])
# import os
# def test_getUserInfo(self,host):
#     url = host + "/api/login"
#     print("测试用例url为：",url)
#
# run_command = "pytest -v -s --cmdhost=https://www.4399.com .\\test_login.py"
# os.system(run_command)
