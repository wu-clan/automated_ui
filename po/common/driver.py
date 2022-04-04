#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from selenium import webdriver

from po.common.log import log


class WebDriver(object):

    def __init__(self, driver=None):
        """
        初始化驱动

        :param driver:
        """
        self.__driver = driver

    @property
    def __firefox_driver(self):
        """
        Firefox driver

        :return:
        """
        try:
            self.__driver = webdriver.Firefox()
            self.__driver.maximize_window()
        except Exception as e:
            log.exception('FireFox Driver need to add environment PATH. please download!')
            raise e
        else:
            log.info('%s : Firefox driver use success !' % (sys._getframe().f_code.co_name))
            return self.__driver

    @property
    def __chrome_driver(self):
        """
        chrome driver

        :return:
        """
        try:

            chrome_options = webdriver.ChromeOptions()
            # 不打开浏览器页面
            # chrome_options.add_argument('headless')
            # 关闭显示：Chrome 正在受自动测试软件的控制 配置。
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            # 关闭提示保存密码的弹框。
            prefs = {"": ""}
            prefs["credentials_enable_service"] = False
            prefs["profile.password_manager_enabled"] = False
            chrome_options.add_experimental_option("prefs", prefs)
            self.__driver = webdriver.Chrome(options=chrome_options)
            self.__driver.maximize_window()
        except Exception as e:
            log.exception('Chrome Driver need to add environment PATH. please download!!')
            raise e
        else:
            log.info('%s : chrome driver use success !' % (sys._getframe().f_code.co_name))
            return self.__driver

    @property
    def __ie_driver(self):
        """
        Ie driver

        :return:
        """
        try:
            self.__driver = webdriver.Ie()
            self.__driver.maximize_window()
        except Exception as e:
            log.exception('IE Driver need to add environment PATH. please download!!')
            raise e
        else:
            log.info('%s : IE driver use success !' % (sys._getframe().f_code.co_name))
            return self.__driver

    def select_browser(self, browser='chrome'):
        """
        浏览器驱动选择

        :param browser:
        :return:
        """
        if browser == "firefox" or browser == "Firefox":
            return self.__firefox_driver
        elif browser == "chrome" or browser == "Chrome":
            return self.__chrome_driver
        elif browser == "ie" or browser == "IE":
            return self.__ie_driver
        else:
            raise ValueError(
                'Error: browser startup error,please check, only these："firefox", "ff", "chrome", "Chrome", "ie", "IE" of one')


web_driver = WebDriver()

__all__ = [
    'web_driver'
]

if __name__ == '__main__':
    print(web_driver.select_browser())
