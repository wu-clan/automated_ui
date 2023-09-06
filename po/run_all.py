#! user/bin/python
# -*- coding: utf-8 -*-
from po.common.test_report import html_report, add_testcase, btf_report
from po.core.get_conf import REPORT_STYLE
from po.utils.send_report.send_email import send_email_report

if __name__ == '__main__':
    try:
        test_suite = add_testcase()
        if REPORT_STYLE == 'btf':
            # BeautifulReport 测试报告
            filename = btf_report(test_suite)

        elif REPORT_STYLE == 'htr':
            # HTMLTestRunner 测试报告
            runner, filename = html_report()
            runner.run(test_suite)
        else:
            raise ValueError('❌ Conf test_report style set error')
    except Exception as e:
        raise e
    else:
        send_email_report(filename)
