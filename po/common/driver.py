#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os

import urllib3  # noqa
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IeService
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

    @property
    def chrome(self) -> webdriver.Chrome:
        """
        chrome driver

        :return:
        """
        try:

            chrome_options = webdriver.ChromeOptions()
            chrome_service = ChromeService(executable_path=ChromeDriverManager().install())  # noqa: E501

            # Options 参数配置
            # https://github.com/GoogleChrome/chrome-launcher/blob/main/docs/chrome-flags-for-tools.md
            arguments = [
                '--disable-extensions',  # 禁用扩展,
                '--disable-features=Translate',  # 禁用翻译
                '--hide-scrollbars',  # 屏幕截图中隐藏滚动条
                '--no-first-run',  # 跳过首次运行向导
                '--disable-background-networking',  # 禁用后台网络服务
                '--disable-sync',  # 禁用同步到 Google 帐户
                '--disable-features=OptimizationHints',  # 禁用优化提示
            ]
            for arg in arguments:
                chrome_options.add_argument(arg)

            # Options 实验选项
            exclude_switches = [
                'enable-automation',  # 关闭显示 “Chrome 正在受自动测试软件的控制”
                'ignore-certificate-errors',  # 忽略证书错误
            ]
            prefs = {
                "credentials_enable_service": False,  # 禁用自动填充凭据（如用户名，密码等）
                "profile.password_manager_enabled": False,  # 禁用浏览器密码管理器功能
            }
            chrome_options.add_experimental_option('excludeSwitches', exclude_switches)
            chrome_options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Google Chrome failed to start')
            raise e
        else:
            log.info('✅ Google Chrome started successfully')
            return driver

    @property
    def edge(self) -> webdriver.Edge:
        """
        edge driver

        :return:
        """
        try:
            edge_service = EdgeService(executable_path=EdgeChromiumDriverManager().install())  # noqa: E501
            driver = webdriver.Edge(service=edge_service)
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Edge failed to start')
            raise e
        else:
            log.info('✅ Edge started successfully')
            return driver

    @property
    def firefox(self) -> webdriver.Firefox:
        """
        Firefox driver

        :return:
        """
        try:
            firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())  # noqa: E501
            driver = webdriver.Firefox(service=firefox_service)
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Firefox failed to start')
            raise e
        else:
            log.info('✅ Firefox started successfully')
            return driver

    @property
    def ie(self) -> webdriver.Ie:
        """
        Ie driver

        :return:
        """
        try:
            ie_service = IeService(executable_path=IEDriverManager().install())  # noqa: E501
            driver = webdriver.Ie(service=ie_service)
            driver.maximize_window()
        except Exception as e:
            log.error('❌ Ie failed to start')
            raise e
        else:
            log.info('✅ Ie started successfully')
            return driver

    def select_browser(self):
        """
        浏览器驱动选择

        :return:
        """
        browser = str(get_conf.BROWSER).lower()
        try:
            driver = getattr(self, browser)
        except Exception:
            raise ValueError(
                '❌ wrong browser selection, please check, only allow one of: ["chrome", "firefox", "edge", ”ie“]'
            )
        log.info('')  # 预留空行
        return driver


web_driver = WebDriver()
