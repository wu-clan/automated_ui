#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import yaml

from po.common.log import log
from po.core import path_conf


class DoYaml(object):

    def __init__(self, filename='...', depend=True):
        """
        初始化 yaml 文件

        :param filename:
        :param depend:
        :return:
        """
        if depend:
            from po.core import get_conf
            self.filename = os.path.join(path_conf.YAML_DATA_PATH, get_conf.PROJECT, filename)
        else:
            self.filename = os.path.join(path_conf.YAML_DATA_PATH, filename)

    @property
    def read_yaml(self):
        """
        读取yaml数据

        :return:
        """
        try:
            with open(self.filename, encoding='utf-8') as f:
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except FileNotFoundError as e:
            log.error('❌ read %s elements failed %s' % (self.filename, e))
            raise e

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
            log.error('❌ write %s data failure %s' % (self.filename, e))
            raise e


if __name__ == '__main__':
    dy = DoYaml(filename='baidu_elements.yaml').read_yaml
    print(dy)
    print(dy['baidu_button'])
