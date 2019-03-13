'''

用例运行级别
模块级（setup_module/teardown_module)开始于模块始末，全局的。

函数级（setup_function/teardown_function）只对函数用例生效

类级（setup__class/teardown_class）只在类中前后运行一次（在类中）

方法级（setup_method/teardown_method）开始于方法始末（在类中）

类里面的（setup/teardown）运行在调用方法的前后



函数式
setup_function/teardown_function

pytest 框架支持函数和类两种用例方式，先看函数里面的前置与后置方法

运行结果是，setup_function>用例>teardown_function>setup_function>用例二




模块级

setup_module / teardown_module是所有用例结束后只执行一次

方法的最开始调用setup_module，最后调用 teardown_module




类级（setup__class/teardown_class）类似上面的模块级，不过要写class，在写方法，都是在一开始和最后调用，但是它运行优先级大于setup_module的
'''
