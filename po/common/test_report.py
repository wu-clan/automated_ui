#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
代码描述: 测试报告（常run_select调用）
"""
import os
import time
import unittest

from BeautifulReport import BeautifulReport

from po.core import path_conf, get_conf
from po.common.log import log
from po.packages.TestRunner import HTMLTestRunner


def test_report():
    """
    HTMLTestRunner 实现的测试报告
    :return:
    """
    if not os.path.exists(path_conf.REPORT_PATH):
        os.makedirs(path_conf.REPORT_PATH)
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = path_conf.REPORT_PATH + '\\' + path_conf.PROJECT_NAME + '_' + currTime + '.html'
    try:
        fp = open(fileName, 'wb')
    except Exception as e:
        log.exception('[%s] open fail, Unable to generate test report' % fileName)
        raise e
    else:
        runner = HTMLTestRunner(stream=fp,
                                title=path_conf.PROJECT_NAME + '_testreport',
                                verbosity=2,
                                tester=get_conf.REPORT_TESTER,
                                description=get_conf.REPORT_DESCRIPTION)
        log.info('Test report generated successfully [%s]' % fileName)
        return runner, fp, fileName


def addTc(tc_path=path_conf.TESTCASE_PATH, rule='test*.py'):
    """
    添加测试用例
    :param tc_path: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(tc_path, rule)
    return discover


def runTc(discover):
    """
    BeautifulReport模块实现测试报告
    :param discover: 测试套件
    :return:
    """
    if not os.path.exists(path_conf.REPORT_PATH):
        os.makedirs(path_conf.REPORT_PATH)
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = path_conf.PROJECT_NAME + '_' + currTime + '.html'
    try:
        result = BeautifulReport(discover)
        # theme四种用法：theme_default theme_cyan theme_candy theme_memories
        result.report(filename=fileName,
                      description=path_conf.PROJECT_NAME + '_testreport',
                      report_dir=path_conf.REPORT_PATH,
                      theme='theme_cyan')
    except Exception as e:
        log.exception('Failed to generate test report')
        raise e
    else:
        log.info('Test report generated successfully [%s]' % fileName)
        return fileName


if __name__ == '__main__':
    suite = addTc(rule='*Tc.py')
    runTc(suite)
