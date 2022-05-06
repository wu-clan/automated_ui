#! user/bin/python
# -*- coding: utf-8 -*-
import unittest

from po.common.test_report import add_tc, run_tc, test_report
from po.core import path_conf
from po.utils.send_email import send_mail

if __name__ == '__main__':
	try:
		"""
		BeautifulReport 测试报告
		"""
		# suite = add_tc()
		# run_tc(suite)

		"""
		HTMLTestRunner 测试报告
		"""
		runner, fp, fileName = test_report()
		test_suite = unittest.defaultTestLoader.discover(path_conf.TESTCASE_PATH)
		runner.run(test_suite)
	except Exception as e:
		print('startup failed ！！！\n\t error info: {}'.format(e))
		raise e
	else:
		send_mail.send()
