# coding:utf-8

import pytest


@pytest.mark.parametrize("x", ["路"])
@pytest.mark.parametrize("y", [2, 3, "云"])
@pytest.mark.parametrize("z", ["鹏"])
def test_foo(x, y, z):
    print(x, y, z)


if __name__ == '__main__':
    pytest.main(["-s", "test_parame_combination.py"])
