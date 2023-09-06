#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import yaml

from po.common.log import log
from po.core import path_conf


class DoYaml(object):

    def __init__(self, filename=..., local_element_file=False):
        """
        初始化 yaml 文件

        :param filename:
        :param local_element_file:
        :return:
        """
        self.local_element_file = local_element_file
        if self.local_element_file:
            from po.core import get_conf
            self.filename = os.path.join(path_conf.YAML_DATA_PATH, get_conf.PROJECT, filename)
        else:
            self.filename = os.path.join(path_conf.YAML_DATA_PATH, filename)

    def read_yaml(self) -> dict:
        """
        读取yaml文件数据

        :return: dict[Any] if element_file=False else {variable_name: element, ...}
        """
        try:
            with open(self.filename, encoding='utf-8') as f:
                if not self.local_element_file:
                    data = yaml.load(f.read(), Loader=yaml.FullLoader)
                else:
                    data = yaml.load(f.read(), Loader=yaml.FullLoader)
                    if data:
                        for key, value in data.items():
                            if not isinstance(value, dict):
                                raise ValueError('❌ Element data parse error, the data type must be dictionary')
                            if ('by' and 'element') not in value.keys():
                                raise ValueError('❌ Element data parse error, the data must contain "by" and "element"')
                            data.update({key: value['element']})
                    else:
                        raise ValueError('❌ Element file data is empty')
        except FileNotFoundError as e:
            log.error(f'❌ Read yaml file error: {e}')
            raise e
        return data

    def write_yaml(self, data, encoding='uft-8', mode='w'):
        """
        写入yaml数据

        :param data: 写入数据
        :param encoding: 文件编码格式
        :param mode: 写入模式
        :return:
        """
        try:
            with open(self.filename, encoding=encoding, mode=mode) as f:
                return yaml.dump(data, stream=f, allow_unicode=True)
        except FileNotFoundError as e:
            log.error(f'❌ Write yaml file error: {e}')
            raise e
