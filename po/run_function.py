#! user/bin/python
# -*- coding: utf-8 -*-
"""
Code description：可单独的测试
"""

import unittest

from po.common.test_report import test_report
from po.test_case.baidu.test_baidu import BaiDu


class RunTcScript(object):

	def __init__(self):
		self.suite = unittest.TestSuite()

	def test_function(self, testClass, testcase):
		"""
		执行指定测试用例
		:param testClass: 测试用例类名
		:param testcase: 测试用例方法名
		:return:
		"""
		self.suite.addTest(testClass(testcase))


if __name__ == '__main__':
	# suite
	suite_tc = RunTcScript()
	suite_tc.test_function(BaiDu, 'test_baidu_s')

	# 1.不输出到测试报告
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite_tc.suite)

	# 2.输出到HTML测试报告
	# runner, fp, filename = test_report()
	# runner.run(suite_tc.suite)
