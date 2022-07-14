#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))  # noqa

from po.common.log import log
from po.common.test_report import test_report
from po.test_case.baidu.test_baidu import BaiDu


class RunTcClass(object):

	def __init__(self):
		self.suites = unittest.TestLoader()
		self.suit = unittest.TestSuite()

	def test_class(self, testcase_class):
		"""
		测试用例类

		:param testcase_class: 测试用例类
		"""
		suites = self.suites.loadTestsFromTestCase(testcase_class)
		self.suit.addTest(suites)


if __name__ == '__main__':
	suite_tc = RunTcClass()

	# 执行测试类
	suite_tc.test_class(BaiDu)

	# 1.不输出到测试报告
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite_tc.suit)

	# 2.输出到HTML测试报告
	# runner, fp, filename = test_report()
	# runner.run(suite_tc.suit)
	# log.info('Test report generated successfully [%s]' % filename)  # 仅使用此报告时将其作为输入输出
