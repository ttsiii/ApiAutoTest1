# coding:utf-8
#heboqiang

import os
import configparser

#获取当前路径下的配置文件
configpath  = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/configs/token.ini")
conf = configparser.ConfigParser()

# conf.read(configpath,encoding="utf-8")
conf.read(configpath,encoding="utf-8-sig")

Environ = conf.get('Environ','environ')
env = conf.get('Environ','env')
#获取配置文件中的key值
zhangsan_token = conf.get('token','zhangsan_token')
lisi_token = conf.get('token','lisi_token')

# print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",token)
# print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",Environ1)

# 获取所有的section
# sections = conf.sections()
#
# print(sections)  # 返回list
# items = conf.items('token')
# print(items)  # list里面对象是元祖
# conf.remove_option('Environ', "environ11")
# items = conf.items('Environ')
# print(items)  # list里面对象是元祖
