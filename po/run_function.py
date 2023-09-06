#! user/bin/python
# -*- coding: utf-8 -*-
import unittest

from po.test_case.baidu.test_baidu import BaiDu


class RunTcFunc:

    def __init__(self):
        self.suite = unittest.TestSuite()

    def run(self, testcase_func, verbosity=1):
        """
        :param testcase_func: 测试用例函数
        :param verbosity:
        """
        if isinstance(testcase_func, list):
            self.suite.addTests(testcase_func)
        else:
            self.suite.addTest(testcase_func)
        runner = unittest.TextTestRunner(verbosity=verbosity)
        runner.run(self.suite)


if __name__ == '__main__':
    func_runner = RunTcFunc()
    func_runner.run(BaiDu('test_baidu_pass'))
