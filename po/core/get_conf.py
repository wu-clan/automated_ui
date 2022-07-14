#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from po.common.do_yaml import DoYaml

__read_config = DoYaml(os.path.join(os.getcwd(), 'core'), 'config.yaml').read_yaml

# 浏览器使用
BROWSER = __read_config['browser']

# 程序主入口
MAIN_PATH = __read_config['main_path']

# 数据库配置信息。
DB_HOST = __read_config['mysql']['host']
DB_PORT = __read_config['mysql']['port']
DB_USER = __read_config['mysql']['user']
DB_PASSWORD = __read_config['mysql']['password']
DB_DATABASE = __read_config['mysql']['database']
DB_CHARSET = __read_config['mysql']['charset']

# 邮件配置
EMAIL_SERVER = __read_config['email']['host_server']
EMAIL_PORT = __read_config['email']['port']
EMAIL_USER = __read_config['email']['user']
EMAIL_PASSWORD = __read_config['email']['password']
EMAIL_SEND_TO = __read_config['email']['send_to']
EMAIL_SSL = __read_config['email']['is_ssl']

# 测试报告配置
REPORT_TESTER = __read_config['test_report']['tester']
REPORT_DESCRIPTION = __read_config['test_report']['description']
