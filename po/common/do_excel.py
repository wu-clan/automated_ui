#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from pylightxl import readxl

from po.common.log import log
from po.core import path_conf, get_conf


class DoExcel(object):

    def __init__(self, filename=..., sheet='Sheet1'):
        """
        初始化 excel 文件

        :param filename:文件名
        :param sheet:表名
        :return:
        """
        try:
            self.file = os.path.join(path_conf.EXCEL_DATA_PATH, get_conf.PROJECT, filename)
            self.workbook = readxl(fn=self.file)
            self.sheet = self.workbook.ws(ws=sheet)
        except Exception as e:
            log.error(f'❌ Init excel file error: {e}')
            raise e

    def read_excel(self) -> dict:
        """
        读取 excel 元素文件

        :return: {variable_name: element, ...}
        """
        data: dict = {}
        try:
            row = self.sheet.maxrow
            if row > 0:
                col2value = self.sheet.col(col=2)
                if len(col2value) != len(set(col2value)):
                    raise ValueError('❌ There are duplicates in Excel variable names')
                for i in range(1, row):
                    data.update({self.sheet.index(row=i + 1, col=2): self.sheet.index(row=i + 1, col=4)})  # noqa: E501
            else:
                raise ValueError('❌ Excel data is empty')
        except Exception as e:
            log.error(f'❌ Read excel file error: {e}')
            raise e
        else:
            return data
