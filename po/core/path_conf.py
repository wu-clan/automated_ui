# -*- coding: utf-8 -*-

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例路径
PROJECT_NAME = sys.argv[1]
TESTCASE_PATH = os.path.join(BASE_DIR, 'test_case', PROJECT_NAME)

# 获取日志路径
LOG_PATH = os.path.join(BASE_DIR, 'report', 'log')

# 获取excel数据路径
EXCEL_PATH = os.path.join(BASE_DIR, 'data', 'test_data')

# 获取yaml数据路径
YAML_PATH = os.path.join(BASE_DIR, 'data', 'test_data')

# 错误截图
FAIL_IMG_PATH = os.path.join(BASE_DIR, 'report', 'image', 'fail')
# 成功截图
PASS_IMG_PATH = os.path.join(BASE_DIR, 'report', 'image', 'pass')

# 测试报告配置
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'test_report')
