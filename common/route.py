from common.read_yaml import get_yaml_filepath


"""----------------member_controller模块api路径------------------"""
"""login接口路径"""
login = get_yaml_filepath(filepath="/member_controller/login.yaml")#读取数据
"""get_auth_code接口路径"""
get_auth_code = get_yaml_filepath(filepath="/member_controller/get_auth_code.yaml")#读取数据
"""register接口路径"""
register = get_yaml_filepath(filepath="/member_controller/register.yaml")#读取数据
"""getmember_info接口路径"""
getmember_info = get_yaml_filepath(filepath="/member_controller/getmember_info.yaml")#读取数据

print(login)

"""----------------receiving模块api路径------------------"""
"""add_shipping_address接口路径"""
add_shipping_address = get_yaml_filepath(filepath="/receiving/add_shipping_address.yaml")#读取数据
"""address_delete接口路径"""
address_delete = get_yaml_filepath(filepath="/receiving/address_delete.yaml")#读取数据
"""address_list接口路径"""
address_list = get_yaml_filepath(filepath="/receiving/address_list.yaml")#读取数据

