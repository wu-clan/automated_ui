#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
代码描述:所有的驱动信息
"""

import sys

from selenium import webdriver

from po.common.log import log


class WDriver(object):

    def __init__(self, driver=None):
        self.driver = driver

    def firefox_driver(self):
        """
        Firefox driver
        :return:
        """
        try:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        except Exception as e:
            log.exception('FireFox Driver need to add environment PATH. please download!')
            raise e
        else:
            log.info('%s : Firefox driver use success !' % (sys._getframe().f_code.co_name))
            return self.driver

    def chrome_driver(self):
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
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
        except Exception as e:
            log.exception('Chrome Driver need to add environment PATH. please download!!')
            raise e
        else:
            log.info('%s : chrome driver use success !' % (sys._getframe().f_code.co_name))
            return self.driver

    def ie_driver(self):
        """
        Ie driver
        :return:
        """
        try:
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
        except Exception as e:
            log.exception('IE Driver need to add environment PATH. please download!!')
            raise e
        else:
            log.info('%s : IE driver use success !' % (sys._getframe().f_code.co_name))
            return self.driver


def select_browser(browser='chrome'):
    if browser == "firefox" or browser == "Firefox":
        return WDriver().firefox_driver()
    elif browser == "chrome" or browser == "Chrome":
        return WDriver().chrome_driver()
    elif browser == "ie" or browser == "IE":
        return WDriver().ie_driver()
    else:
        raise ValueError('Error: browser startup error,please check, only these：'
                         '"firefox", "ff", "chrome", "Chrome", "ie", "IE" of one')


__all__ = [
    'select_browser'
]

if __name__ == '__main__':
    print(select_browser())
