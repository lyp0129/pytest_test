
'''

pytest.mark.skip 可以标记无法运行的测试功能，或者希望失败的测试功能


skip 意味着只有在满足某些条件时才希望测试通过。


xfail意味着希望测试由于某种原因而失败，例子：功能的测试尚未实施，或尚未修复的错误。当测试通过时尽管预计会失败（标有pytest.mark.xfail）
它是个xpass，将在测试摘要中报告


'''




'''
skip

跳过测试函数的最简单方法是使用跳过装饰器标记它，可以传递一个可选的原因
@pytest.mark.skip(reason="no way of currently testing this")
                （写失败原因）

def test_the()


'''

'''

或者，也可以通过调用来在测试执行或设置期间强制跳过 pytest.skip(reason)功能

def test_function():

if not vaild_config():

pytest.skip("unsupported configuration")
           （写失败原因）


'''

'''

也可以使用pytest.skip（reason，allow_module_level=True）跳过整个模块级别：
                    (reason:跳过的原因)

import pytest

if not pytest.config.getoption("-- custom-flag"):

pytest.skip("--custom -flag is missing, skipping tests",allow_module_lever =True)

'''


'''

如果希望有条件地跳过某些内容，则可以使用skipif代替。

标记测试的示例在python3.6之前的解释器上运行时要跳过的函数

import sys

@pytest.mark.skipid(sys.version_info<(3.6),reason="requires python 3.6 or higher")

def test_function():


'''




'''

skip类或模块



'''







