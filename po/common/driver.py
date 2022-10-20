#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os

import urllib3  # noqa
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

from po.common.log import log
from po.core import get_conf


class WebDriver:
    # webdriver-manager 配置: https://github.com/SergeyPirogov/webdriver_manager
    os.environ['WDM_LOG'] = str(logging.NOTSET)
    os.environ['WDM_SSL_VERIFY'] = '0'
    urllib3.disable_warnings()

    def __init__(self, webdriver_path='../webdriver'):
        """
        初始化驱动

        :param webdriver_path: 浏览器驱动存放位置
        """
        self.__path = webdriver_path

    @property
    def chrome(self):
        """
        chrome driver

        :return:
        """
        try:

            chrome_options = webdriver.ChromeOptions()
            # 不打开浏览器页面
            # chrome_options.add_argument('headless')
            # 关闭显示：Chrome 正在受自动测试软件的控制配置
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            # 关闭提示保存密码的弹框。
            prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
            chrome_options.add_experimental_option("prefs", prefs)
            # 忽略日志
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            driver = webdriver.Chrome(
                executable_path=ChromeDriverManager(path=self.__path).install(),
                options=chrome_options
            )
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Error calling google chrome')
            raise e
        else:
            log.info('Chrome driver use success')
            return driver

    @property
    def edge(self):
        """
        edge driver

        :return:
        """
        try:
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager(path=self.__path).install())
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Error calling edge browser')
            raise e
        else:
            log.info('Edge driver use success')
            return driver

    @property
    def firefox(self):
        """
        Firefox driver

        :return:
        """
        try:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager(path=self.__path).install())
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Error calling firefox browser')
            raise e
        else:
            log.info('Firefox driver use success')
            return driver

    @property
    def ie(self):
        """
        Ie driver

        :return:
        """
        try:
            driver = webdriver.Ie(executable_path=IEDriverManager(path=self.__path).install())
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Error calling ie browser')
            raise e
        else:
            log.info('IE driver use success')
            return driver

    def select_browser(self):
        """
        浏览器驱动选择

        :return:
        """
        driver = str(get_conf.BROWSER).lower()
        try:
            return getattr(self, driver)
        except Exception:
            raise AttributeError(
                f'❌ wrong browser selection, please check, only allow one of: chrome, firefox, edge, ie'
            )


web_driver = WebDriver()
