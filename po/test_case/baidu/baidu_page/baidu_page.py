#!/usr/bin/python3
# -*- coding: utf-8 -*-
from po.common.base_page import BasePage
from po.common.do_excel import DoExcel
from po.common.do_yaml import DoYaml
from po.common.myunit import Unit


class BaiDuPage(Unit, BasePage):
    """
    存放元素 or 公共操作
    Note: Unit 必须放在首位继承
    """
    # 定义定位元素有两种方式，一种是从文件读取，一种是内部定义
    # 建议一个页面类中只使用一种方式，会更方便进行维护

    # 方式一：文件读取定位元素
    baidu_elements_excel = DoExcel('baidu_elements.xlsx').read_excel()
    baidu_elements_yaml = DoYaml('baidu_elements.yaml', local_element_file=True).read_yaml()
    global_elements = DoYaml('global_elements.yaml').read_yaml()
    # 搜索按钮
    search_btn = ['id', baidu_elements_excel['baidu_button']]
    # ignore: 额外测试
    search_btn_test1 = ['id', baidu_elements_yaml['baidu_button']]
    search_btn_test2 = ['id', global_elements['baidu_button']]

    # 方式二：内部定义定位元素
    # 搜索框
    source = ['id', 'kw']

    # 定义关键子
    def click_btn(self):
        """
        点击搜索按钮

        :return:
        """
        self.click(self.search_btn)
