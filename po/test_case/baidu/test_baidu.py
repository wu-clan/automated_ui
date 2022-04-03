#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from po.common.doyaml import DoYaml
from po.test_case.baidu.baidu_page.baidu_page import Baidu

yamlData = DoYaml(filename='universal_elements.yaml').read_yaml()


class BaiDu(Baidu):
    """测试百度"""

    def test_baidu_s(self):
        """成功用例"""
        self.send_keys(Baidu.source, '测试')
        self.click(Baidu.source_btn)
        self.save_screenshot('test_pass.png')

    def test_baidu_f(self):
        """失败用例"""
        ele = ['xpath', yamlData['baidu_button']]
        result = self.iselement_exist(ele)
        self.save_screenshot('test_fail.png')
        self.assertTrue(result, '未找到元素 %s' % ele)

    @unittest.skip('强制跳过')
    def test_baidu_skip(self):
        """跳过用例"""
        self.send_keys(Baidu.source, '测试')
        self.click(Baidu.source_btn)

    def test_baidu_e(self):
        """错误用例"""
        self.send_keys(['name', 'xxxxxxx'], '测试')
