#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from po.common.base_page import BasePage
from po.common.driver import web_driver
from po.common.log import log
from po.core import get_conf


class MyUnitTest(unittest.TestCase):
    """
    Ps:单元测试框架,封装基类,所有test_case继承此类,自动获得所有unittest方法
    """

    def __init__(self, *args, **kwargs):
        # 继承 unittest.TestCase 的__init__,尤为重要
        unittest.TestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(cls):
        """
        一个测试类(文件)仅打开一次浏览器, 节约了每个用例都要打开一次浏览器的时间

        :return:
        """
        cls.driver = web_driver.select_browser(get_conf.BROWSER)

    def setUp(self):
        """
        每个测试用例都会从主入口进行访问

        :return:
        """
        self.open = BasePage(self.driver)
        self.open.open()
        log.info(f'----------------- Running case: {self._testMethodName} -----------------')

    def tearDown(self):
        log.info('end \n')

    @classmethod
    def tearDownClass(cls):
        cls().driver.quit()
