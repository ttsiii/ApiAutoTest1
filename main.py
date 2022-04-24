# coding=utf-8
import pytest
import os
import shutil
from common.logger import Logger
from until.clear_results import clear_allure
from random import randint

if __name__ == '__main__':
    Logger.info(r"""
                                                          _ooOoo_
                                                         o8888888o
                                                         88" . "88
                                                         (| -_- |)
                                                          O\ = /O
                                                      ____/`---'\____
                                                    .   ' \\| |// `.
                                                     / \\||| : |||// \
                                                   / _||||| -:- |||||- \
                                                     | | \\\ - /// | |
                                                   | \_| ''\---/'' | |
                                                    \ .-\__ `-` ___/-. /
                                                 ___`. .' /--.--\ `. . __
                                              ."" '< `.___\_<|>_/___.' >'"".
                                             | | : `- \`.;`\ _ /`;.`/ - ` : | |
                                               \ \ `-. \_ __\ /__ _/ .-` / /
                                       ======`-.____`-.___\_____/___.-`____.-'======
                                                          `=---='

                                       .............................................
                                              佛祖保佑             永无BUG
                                       .............................................
""")

    """解决allure报告缓存和Jenkins无文件报错"""
    clear_allure()

    # pytest.main(['-m','smoke'])
    # pytest.main(["-s",'--workers=1', '--tests-per-worker=4'])
    pytest.main()
    #测试报告本地静态数据生成--allure generate ./allure-xml -o ./allure-result
    os.system(r"allure generate ./report/allure-results -o ./report/allure-report --clean")


    # port = randint(1000, 9999)
    # os.system('allure open ./report/allure-report --port {}'.format(port))  # 打开报告

#失败重试
# • 测试失败后要重新运行n次，要在重新运行之间添加延迟时 间，间隔n秒再运行。
# • 执行:
# • 安装:pip install pytest-rerunfailures
# • pytest -v - -reruns 5 --reruns-delay 1 —每次等1秒 重试5次



