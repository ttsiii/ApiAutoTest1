import pytest
import os
import shutil


# shutil.rmtree( src )   #递归删除一个目录以及目录内的所有内容
# os.makedirs() 方法用于递归创建目录。
"""解决allure报告缓存和Jenkins无文件报错"""
def clear_allure():
    filepath = (os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/report/allure-results/")
    if os.path.exists(filepath):
        shutil.rmtree("{}".format(filepath))
        os.makedirs("{}".format(filepath))
    else:
        os.makedirs("{}".format(filepath))
    path_report = (os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/report/allure-report")
    if os.path.exists(path_report):
        shutil.rmtree("{}".format(path_report))

if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(__file__)) + "/report/allure-results/")