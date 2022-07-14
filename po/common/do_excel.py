#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

import xlrd

from po.core import path_conf
from po.common.log import log


class DoExcel(object):

    def __init__(self, filename='...', sheet='Sheet1'):
        """
        初始化 excel 文件

        :param filename:文件名
        :param sheet:表名
        :return:
        """
        try:
            self.file = os.path.join(path_conf.EXCEL_PATH, filename)
            self.workbook = xlrd.open_workbook(self.file)
            self.sheet = self.workbook.sheet_by_name(sheet)
        except Exception as e:
            log.error('Error: init excel file \n %s' % e)
            raise e

    @property
    def read_excel(self):
        """
        读取 excel 文件

        :return:
        """
        data = None
        try:
            # 获取总行,列数
            rows = self.sheet.nrows
            cols = self.sheet.ncols
            if rows > 1:
                # 获取表格中的第二列数据, 应为变量名
                keys = self.sheet.col_values(1, 1)
                values = self.sheet.col_values(3, 1)
                # 获取文档剩下所有内容
                for _ in range(1, cols):
                    # key, value组合为字典
                    data = dict(zip(keys, values))
            else:
                log.warning('Data table has no data!')
                return data
        except Exception as e:
            log.error('Error: read value from excel file')
            raise e
        else:
            return data


if __name__ == '__main__':
    de = DoExcel('baidu_elements.xlsx').read_excel
    print(de)
    print(de['baidu_button'])
