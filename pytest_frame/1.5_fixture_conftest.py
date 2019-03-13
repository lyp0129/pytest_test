# coding:utf-8
'''

setup 和 teardown可以实现在测试用例之前或者之后加一些操作，但是这种是整个脚步全局生效的。

但是想要用例1 登陆，用例2不登陆了，就没办法用setup和teardown，现在自定义测试用例


fixture 优势

命名方式灵活，不局限于setup和teardown这几个命名

conftest.py配置里可以实现数据共享，不需要import 就能自动找一些配置

scope=“module” 可以实现多个.py夸文件共享前置



fixture(scope="function",params=None,autouse=False,ids=None,name=None):

可以使用此装饰器（带或不带参数）来定义fixture功能。fixture功能的名称可以在以后使用，引用它会在运行测试之前调用它：test模块或类可以使用pytest.mark.usefixures


arg scope:scop有四个级别的参数 “function（默认）”，“class”，“module（整个py文件都生效）”，“session”

arg params： 一个可选的参数列表，它将导致多个参数调用fixture 功能和所有测试使用它

arg autouse： 如果为true，则为所有测试激活fixture func 可以看到它。如果为false（默认值）则显示需要参考来激活fixture

arg ids：每个字符串 id的列表，每个字符串对于params这样他们就是测试id的一部分。如果没有提供id他们将从params自动生成

arg name ：fixture的名称。这默认为装饰函数名称。


conftest.py配置

 多个用例调用一个登录功能，如果有多个.py的文件都需要调用这个登录功能的话，那就不能把登陆写到用例里面去了。

此时应该要有一个配置文件，单独管理一些预置的操作场景，pytest里面默认读取conftest.py


conftest.py 配置脚本名称是固定的，不能改名称

conftest.py 与运行的用例在同一个package下，并且有
__init__ .py文件

不需要import导入conftest.py ，pytest用例会自动查找


'''

import pytest


# 不带参数时默认scope="function"

@pytest.fixture()
def login():
    print("输入账号,密码先登陆")


def test_s(login):
    print("用例1：登陆之后其他动作")


def test_s2():
    print("用例2：不用登陆")


def test_s3(login):
    print("用例3：登陆之后其他动作233")


if __name__ == '__main__':
    pytest.main(["-s", "1.5_fixture_conftest.py"])
