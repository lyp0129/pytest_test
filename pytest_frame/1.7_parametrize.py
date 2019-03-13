'''

pytest.mark.parametrize 装饰器可以实现测试用例参数化

还可以做参数组合
'''

import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print(x, y)


if __name__ == '__main__':
    pytest.main(["", ""])
