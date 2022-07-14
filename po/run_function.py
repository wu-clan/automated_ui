#! user/bin/python
# -*- coding: utf-8 -*-
import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))  # noqa

from po.common.log import log
from po.common.test_report import test_report
from po.test_case.baidu.test_baidu import BaiDu


class RunTcFunc(object):

    def __init__(self):
        self.suite = unittest.TestSuite()

    def test_function(self, testcase_class, testcase_func):
        """
        测试用例函数

        :param testcase_class: 测试用例类名
        :param testcase_func: 测试用例函数名
        :return:
        """
        self.suite.addTest(testcase_class(testcase_func))


if __name__ == '__main__':
    suite_tc = RunTcFunc()

    # 执行测试用例方法
    suite_tc.test_function(BaiDu, 'test_baidu_p')

    # 1.不输出到测试报告
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_tc.suite)

    # 2.输出到HTML测试报告
    # runner, fp, filename = test_report()
    # runner.run(suite_tc.suite)
    # log.info('Test report generated successfully [%s]' % filename)  # 仅使用此报告时将其作为输入输出
