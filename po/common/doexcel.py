#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
代码说明:读取date文件 excel.xlsx 的值
"""

import os

import xlrd

from po.core import path_conf
from po.common.log import log


class ReadExcel(object):

    def __init__(self, fileName='_template.xlsx', sheetName='elementsInfo'):
        """
        初始化类
        :param fileName:文件名
        :param sheetName:表名
        """
        try:
            self.dataFile = os.path.join(path_conf.EXCEL_PATH, fileName)
            self.workBook = xlrd.open_workbook(self.dataFile)
            self.sheetName = self.workBook.sheet_by_name(sheetName)
        except Exception as e:
            log.error('Error: init class ReadExcel \n %s' % e)
            raise e

    def readExcel(self, row_num, col_num):
        """
        读取excel文件
        :param row_num:行数
        :param col_num:列数
        :return: 返回值
        """
        try:
            value = self.sheetName.cell(row_num, col_num).value
        except Exception:
            log.error('Error: read value from excel file')
            raise
        else:
            return value


if __name__ == '__main__':
    cellValue = ReadExcel().readExcel(1, 3)
    print(cellValue)
