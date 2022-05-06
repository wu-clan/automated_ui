#! user/bin/python
# -*- coding: utf-8 -*-
import unittest

from po.common.test_report import test_report
from po.test_case.baidu.test_baidu import BaiDu


class RunTcFunc(object):

	def __init__(self):
		self.suite = unittest.TestSuite()

	def test_function(self, testCaseClass, testcase_func):
		"""
		测试用例函数
		:param testCaseClass: 测试用例类名
		:param testcase_func: 测试用例函数名
		:return:
		"""
		self.suite.addTest(testCaseClass(testcase_func))


if __name__ == '__main__':
	suite_tc = RunTcFunc()

	# 执行测试用例方法
	suite_tc.test_function(BaiDu, 'test_baidu_s')

	# 1.不输出到测试报告
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite_tc.suite)

	# 2.输出到HTML测试报告
	# runner, fp, filename = test_report()
	# runner.run(suite_tc.suite)
