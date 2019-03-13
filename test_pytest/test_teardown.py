# coding:utf-8

'''
用yield来触发teardown
'''
import pytest

@pytest.fixture(scope="module")

def open():

    print("打开浏览器，并且打开百度首页")

    yield

    print("执行teardown！")
    print("最后关闭浏览器")

def test_s(open):

    print("用例1：搜索python1")

def test_s2():

    print("用例2：搜索python2")


@pytest.mark.skip
def test_3(open):

    print("用例1：搜索python3")



if __name__ == '__main__':
    pytest.main(["-s", "test_teardown.py"])
