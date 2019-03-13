# coding:utf-8

import pytest

'''

在pycharm里运行pytest

file->setting->Tools->Python integrated Tool->项目名称->Default test runner -> 选择py.test

'''

if __name__ == '__main__':
    pytest.main(["-s", "1.3_pycharm_run_pytest.py"])

# 这种方式运行
