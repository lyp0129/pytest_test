# coding:utf-8

'''

简单讲就是世纪结果和期望结果去对比，符合预期那就测试pass，不符合预期就faild

'''


def f():
    return 3


def test_function():
    assert f() == 4
