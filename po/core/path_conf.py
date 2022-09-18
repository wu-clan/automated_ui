#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例路径
TESTCASE_PATH = os.path.join(BASE_DIR, 'test_case')

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, 'log')

# 测试数据路径
DATA_PATH = os.path.join(BASE_DIR, 'data')

# excel数据路径
EXCEL_DATA_PATH = os.path.join(DATA_PATH, 'test_data')

# yaml数据路径
YAML_DATA_PATH = os.path.join(DATA_PATH, 'test_data')

# 错误截图
FAIL_IMG_PATH = os.path.join(BASE_DIR, 'report', 'image', 'fail')

# 成功截图
PASS_IMG_PATH = os.path.join(BASE_DIR, 'report', 'image', 'pass')

# 测试报告配置
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'html_report')
