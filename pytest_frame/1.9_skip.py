
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

'''


