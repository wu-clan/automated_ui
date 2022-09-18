#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from XTestRunner import HTMLTestRunner

from po.common.log import log
from po.core import path_conf, get_conf
from po.utils.time_control import get_current_time


def html_report():
    """
    HTMLTestRunner 实现的测试报告

    :return:
    """

    filename = os.path.join(path_conf.REPORT_PATH, get_conf.PROJECT + '_' + get_current_time() + '.html')
    try:
        if not os.path.exists(path_conf.REPORT_PATH):
            os.makedirs(path_conf.REPORT_PATH)
        fp = open(filename, 'wb')
    except Exception as e:
        log.error('❌ [%s] open fail, Unable to generate test report' % filename)
        raise e
    else:
        runner = HTMLTestRunner(
            stream=fp,
            title=get_conf.PROJECT + '_testreport',
            verbosity=2,
            tester=get_conf.REPORT_TESTER,
            description=get_conf.REPORT_DESCRIPTION,
            language='zh-CN'
        )
        return runner, fp, filename


def add_testcase(testcase_path=os.path.join(path_conf.TESTCASE_PATH, get_conf.PROJECT), rule='test_*.py'):
    """
    添加测试用例

    :param testcase_path: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(testcase_path, rule)
    return discover


def btf_report(discover):
    """
    BeautifulReport 实现测试报告

    :param discover: 测试套件
    :return:
    """
    filename = os.path.join(get_conf.PROJECT + '_' + get_current_time() + '.html')
    try:
        if not os.path.exists(path_conf.REPORT_PATH):
            os.makedirs(path_conf.REPORT_PATH)
        result = BeautifulReport(discover)
        # theme四种用法：theme_default theme_cyan theme_candy theme_memories
        result.report(
            filename=filename,
            description=get_conf.PROJECT + '_testreport',
            report_dir=path_conf.REPORT_PATH,
            theme='theme_cyan'
        )
    except Exception as e:
        log.error('❌ [%s] open fail, Unable to generate test report' % filename)
        raise e
    else:
        return filename
