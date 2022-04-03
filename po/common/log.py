#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from loguru import logger

from po.core import path_conf


class Logger:

    @staticmethod
    def log():
        """
        :return: loguru’s logger
        """
        # 判定文件夹
        if not os.path.exists(path_conf.LOG_PATH):
            os.makedirs(path_conf.LOG_PATH)

        # 日志文件名称
        log_file = os.path.join(path_conf.LOG_PATH, "po.log")

        # loguru日志
        logger.add(
            log_file,
            level="DEBUG",
            rotation='00:00',
            retention="7 days",
            encoding='utf-8',
            enqueue=True,
            backtrace=True,
            diagnose=True
        )

        return logger


log = Logger().log()
