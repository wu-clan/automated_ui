#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from po.test_case.baidu.test_baidu import BaiDu


class TcClassRunner:

    def __init__(self):
        self.loader = unittest.TestLoader()
        self.suite = unittest.TestSuite()

    def run(self, testcase_class, verbosity=1):
        """
        :param testcase_class: 测试用例类
        :param verbosity:
        """
        if isinstance(testcase_class, list):
            for i in testcase_class:
                test = self.loader.loadTestsFromTestCase(i)
                self.suite.addTest(test)
        else:
            test = self.loader.loadTestsFromTestCase(testcase_class)
            self.suite.addTest(test)

        runner = unittest.TextTestRunner(verbosity=verbosity)
        runner.run(self.suite)


if __name__ == '__main__':
    crunner = TcClassRunner()
    crunner.run(BaiDu)
