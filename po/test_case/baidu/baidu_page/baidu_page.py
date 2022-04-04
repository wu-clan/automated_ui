#!/usr/bin/python3
# -*- coding: utf-8 -*-

from po.common.base_page import BasePage
from po.common.doexcel import DoExcel
from po.common.doyaml import DoYaml
from po.common.myunit import MyUnitTest


class BaiDuPage(MyUnitTest, BasePage):
    """
    存放元素 or 公共操作
    切记: MyUnitTest 必须放在首位继承,这尤为重要
    """

    # 获取文件中的定位元素
    # 返回为 {'key': 'element'} 形式
    excel_data = DoExcel(filename='baidu_elements.xlsx').read_excel
    yaml_data = DoYaml(filename='universal_elements.yaml').read_yaml

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