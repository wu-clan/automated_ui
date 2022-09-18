#! user/bin/python
# -*- coding: utf-8 -*-
from po.common.log import log
from po.common.test_report import html_report, add_testcase
from po.utils.send_report.send_email import SendMail

if __name__ == '__main__':
    try:
        """
        BeautifulReport 测试报告
        """
        # test_suite = add_testcase()
        # filename = btf_report(test_suite)

        """
        HTMLTestRunner 测试报告
        """
        test_suite = add_testcase()
        runner, fp, filename = html_report()
        runner.run(test_suite)
    except Exception as e:
        log.error('❌ 运行异常')
        raise e
    else:
        send_email = SendMail(filename)
        send_email.send()
