#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import yaml

from po.common.log import log
from po.core import path_conf


class DoYaml(object):

    def __init__(self, path=path_conf.YAML_PATH, filename='...'):
        self.filename = os.path.join(path, filename)

    def read_yaml(self):
        """
        读取yaml数据
        :return:
        """
        try:
            with open(self.filename, encoding='utf-8') as f:
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except FileNotFoundError as e:
            log.error('读取 %s 元素失败 \n %s' % (self.filename, e))
            raise e

    def write_yaml(self, data, encoding='uft-8'):
        """
        写入yaml数据
        :param data: 数据
        :param encoding: 编码格式
        :return:
        """
        try:
            with open(self.filename, encoding=encoding, mode='w') as f:
                return yaml.dump(data, stream=f, allow_unicode=True)
        except FileNotFoundError as e:
            log.error('写入 %s 数据失败 \n %s' % (self.filename, e))
            raise e


if __name__ == '__main__':
    dy = DoYaml().read_yaml()
    print(dy)
    print(dy['baidu_button'])
