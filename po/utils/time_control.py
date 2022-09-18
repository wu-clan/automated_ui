#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime


def get_current_time(filename_style: str = '_') -> str:
    """
    获取当前时间

    :param filename_style:
    :return:
    """
    return datetime.datetime.now().strftime(f'%Y-%m-%d %H{filename_style}%M{filename_style}%S')


def get_current_timestamp() -> str:
    """
    :return: 当前时间戳
    """
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f')
