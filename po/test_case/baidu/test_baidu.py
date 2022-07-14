#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from selenium.common.exceptions import TimeoutException

from po.test_case.baidu.baidu_page.baidu_page import BaiDuPage


class BaiDu(BaiDuPage):
    """测试百度"""

    def test_baidu_p(self):
        """ 成功用例 """
        self.send_keys(self.source, '测试')
        self.click_btn()
        self.save_screenshot('test_pass.png')

    def test_baidu_f(self):
        """ 失败用例 """
        global result
        ele = ['xpath', self.yaml_data['baidu_button']]
        try:
            result = self.is_element_exist(ele)
        except TimeoutException:
            self.save_screenshot('test_fail.png')
            self.assertTrue(result, '未找到元素 %s' % ele)

    @unittest.skip('强制跳过')
    def test_baidu_s(self):
        """ 跳过用例 """
        self.send_keys(self.source, '测试')
        self.click_btn()

    def test_baidu_e(self):
        """ 错误用例 """
        self.send_keys(['name', 'xxxxxxx'], '测试')
