#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from po.test_case.baidu.baidu_page.baidu_page import BaiDuPage


class BaiDu(BaiDuPage):
    """ 测试百度 """

    def test_baidu_pass(self):
        """ 成功用例 """
        self.send_keys(self.source, '测试')
        self.click_btn()
        self.save_screenshot('test_pass.png')

    def test_baidu_fail(self):
        """ 失败用例 """
        ele = ['xpath', self.search_btn]
        result = self.is_element_exist(ele)
        if not result:
            self.save_screenshot('test_fail.png')
        self.assertTrue(result, '元素不存在')

    @unittest.skip
    def test_baidu_skip(self):
        """ 跳过用例 """
        self.send_keys(self.source, '测试')
        self.click_btn()

    def test_baidu_error(self):
        """ 错误用例 """
        self.send_keys(['name', 'xxx'], '测试')
