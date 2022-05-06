#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date : 2021-04-14
# @PRODUCT_NAME :  PyCharm

import unittest

from po.common.test_report import test_report
from po.test_case.baidu.test_baidu import BaiDu


class RunTcClass(object):

	def __init__(self):
		self.suites = unittest.TestLoader()
		self.suit = unittest.TestSuite()

	def test_class(self, testCaseClass):
		"""
		测试用例类
		:param testCaseClass: 测试用例类
		"""
		suites = self.suites.loadTestsFromTestCase(testCaseClass)
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
