#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from po.common.base_page import BasePage
from po.common.do_excel import DoExcel
from po.common.do_yaml import DoYaml
from po.common.myunit import Unit
from po.core.path_conf import DATA_PATH


class BaiDuPage(Unit, BasePage):
    """
    存放元素 or 公共操作
    切记: Unit 必须放在首位继承, 这尤为重要
    """

    # 获取文件中的定位元素
    # 返回为 {'key': 'element'} 形式
    excel_data = DoExcel('baidu_elements.xlsx').read_excel
    yaml_data = DoYaml('global_elements.yaml', depend=False).read_yaml

    # 定义定位元素
    # 搜索框
    source = ['id', 'kw']
    # 搜索按钮
    source_btn = ['id', excel_data['baidu_button']]

    # 定义关键子
    def click_btn(self):
        """
        点击搜索按钮

        :return:
        """
        self.click(self.source_btn)
