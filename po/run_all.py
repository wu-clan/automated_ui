#! user/bin/python
# -*- coding: utf-8 -*-

"""
Code description：自动化测试所有
"""
from po.common.test_report import *
from po.utils.send_email import send_mail

if __name__ == '__main__':
	try:
		"""
		BeautifulReport 测试报告
		"""
		# suite = addTc()
		# runTc(suite)

		"""
		HTMLTestRunner 测试报告
		"""
		runner, fp, fileName = test_report()
		test_suite = unittest.defaultTestLoader.discover(path_conf.TESTCASE_PATH)
		runner.run(test_suite)
	except Exception as e:
		print('运行出错！！！please check！！！')
		raise e
	else:
		send_mail.send()
