'''

在用例前加前置条件，相当于setup，那teardown怎么触发呢？用yidle来唤醒teardown


如果其中一个用例出现异常，不影响yield后面的teardown
'''