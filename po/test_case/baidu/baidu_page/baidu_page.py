#!/usr/bin/python3
# -*- coding: utf-8 -*-

from po.common.base_page import BasePage
from po.common.myunit import MyUnitTest


class Baidu(MyUnitTest, BasePage):
    """
    存放元素 or 公共操作
    切记: MyUnitTest 必须放在首位继承,这尤为重要
    """
    # 搜索框
    source = ['id', 'kw']
    # 搜索按钮
    source_btn = ['id', 'su']
