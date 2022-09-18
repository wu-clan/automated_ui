#! user/bin/python
# -*- coding: utf-8 -*-
import unittest

from po.test_case.baidu.test_baidu import BaiDu


class RunTcFunc(object):

    def __init__(self):
        self.suite = unittest.TestSuite()

    def run(self, testcase_class_func):
        """
        测试用例函数

        :param testcase_class_func: 测试用例类函数
        :return:
        """
        if isinstance(testcase_class_func, list):
            self.suite.addTests(testcase_class_func)
        else:
            self.suite.addTest(testcase_class_func)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite_tc.suite)


if __name__ == '__main__':
    suite_tc = RunTcFunc()
    suite_tc.run(BaiDu('test_baidu_pass'))
