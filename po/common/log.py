#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

from loguru import logger

from po.core.path_conf import LOG_PATH


class Logger:

    @staticmethod
    def log():
        """
        :return: loguru’s logger
        """
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)

        log_file = os.path.join(LOG_PATH, "ui_test.log")

        # 清除 logger 配置
        logger.remove()

        # 控制台输出
        logger.add(
            sys.stdout,
            format="{time:YYYYMMDD HH:mm:ss.SSS} | <level>{level: <8}</level> | <level>{message}</level>",
        )

        # 文件输出
        logger.add(
            log_file,
            format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>',
            level="DEBUG",
            rotation='00:00',
            retention="7 days",
            encoding='utf8',
            enqueue=True,
            backtrace=True,
            diagnose=False,
            catch=True,
        )

        return logger


log = Logger().log()
