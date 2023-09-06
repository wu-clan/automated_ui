#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

from po.common.log import log
from po.core import path_conf, get_conf
from po.enums.by import ByType


class BasePage:

    def __init__(self, driver: webdriver.Remote, url=get_conf.MAIN_PATH):
        """
        初始化驱动信息和测试主入口

        :param driver:
        :param url:
        """
        self.driver = driver
        self.base_url = url

    def open(self):
        """
        打开程序主入口

        :return:
        """
        try:
            self.driver.get(self.base_url)
        except Exception as e:
            log.exception(e)
            raise ValueError('❌ %s Address access error, Please check！' % self.base_url)
        log.info('%s > > Loading succeeded!' % self.base_url)

    def find_element_wait(self, locator: tuple, timeout=5, poll_frequency=0.5):
        """
        显示等待查找给定 By 策略和定位器的元素,元素必须为非隐藏,可能时首选

        - e.g.: find_element_wait((By.XPATH, 'kw'))

        :param locator: 元素定位
        :param timeout: 显示等待超时时长
        :param poll_frequency: 检测的间隔步长，默认为0.5s
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException as e:
            log.error('❌ Find element timeout in %ss: %s', timeout, e)
            raise e
        else:
            return self.driver.find_element(*locator)

    def find_elements_wait(self, locator: tuple, timeout=5, poll_frequency=0.5):
        """
        显示等待查找给定 By 策略和定位器的多个元素,元素必须为非隐藏,可能时首选

        - example: find_elements_wait(By.XPATH, 'kw')

        :param locator: 元素定位
        :param timeout: 显示等待超时时长
        :param poll_frequency: 检测的间隔步长，默认为0.5s
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException as e:
            log.error('❌ find element timeout in %ss: %s', timeout, e)
            raise e
        else:
            return self.driver.find_elements(*locator)

    def is_element_exist(self, *locator, timeout=5, poll_frequency=0.5) -> bool:
        """
        显示等待元素判断元素是否存在于dom

        :param timeout: 显示等待超时时长
        :param poll_frequency: 检测的间隔步长，默认为0.5s
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(*locator))
        except Exception:  # noqa
            return False
        else:
            return True

    def find_element(self, selector: list):
        """
        定位元素

        :param selector: 定位方式及定位表达式, e.g.: ['id', 'kw']
        :return:
        """
        by = selector[0]
        value = selector[1]
        element = None
        if by in ByType.get_member_values():
            try:
                if by == ByType.ID:
                    element = self.driver.find_element(By.ID, value)
                elif by == ByType.NAME:
                    element = self.driver.find_element(By.NAME, value)
                elif by == ByType.CLASS_NAME:
                    element = self.driver.find_element(By.CLASS_NAME, value)
                elif by == ByType.TAG_NAME:
                    element = self.driver.find_element(By.TAG_NAME, value)
                elif by == ByType.LINK_TEXT:
                    element = self.driver.find_element(By.LINK_TEXT, value)
                elif by == ByType.PARTIAL_LINK_TEXT:
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
                elif by == ByType.CSS_SELECTOR:
                    element = self.driver.find_element(By.CSS_SELECTOR, value)
                elif by == ByType.XPATH:
                    element = self.driver.find_element(By.XPATH, value)
            except NoSuchElementException as e:
                log.error("❌ {}: {}".format(value, e.msg))
                raise e
            else:
                return element
        else:
            raise ValueError('❌ by value error, please use: %s' % ByType.get_member_values())

    def find_elements(self, selector: list):
        """
        定位多个元素

        :param selector: 定位方式及定位表达式, example: ['id', 'kw']
        :return:
        """
        by = selector[0]
        value = selector[1]
        element = None
        if by in ByType.get_member_values():
            try:
                if by == ByType.ID:
                    element = self.driver.find_elements(By.ID, value)
                elif by == ByType.NAME:
                    element = self.driver.find_elements(By.NAME, value)
                elif by == ByType.CLASS_NAME:
                    element = self.driver.find_elements(By.CLASS_NAME, value)
                elif by == ByType.TAG_NAME:
                    element = self.driver.find_elements(By.TAG_NAME, value)
                elif by == ByType.LINK_TEXT:
                    element = self.driver.find_elements(By.LINK_TEXT, value)
                elif by == ByType.PARTIAL_LINK_TEXT:
                    element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, value)
                elif by == ByType.CSS_SELECTOR:
                    element = self.driver.find_elements(By.CSS_SELECTOR, value)
                elif by == ByType.XPATH:
                    element = self.driver.find_elements(By.XPATH, value)
            except NoSuchElementException as e:
                log.error("❌ {}: {}".format(value, e.msg))
                raise e
            else:
                return element
        else:
            raise ValueError('❌ by value error, please use: %s' % ByType.get_member_values())

    def element_wait(self, selector: list, timeout=5, poll_frequency=0.5) -> bool:
        """
        显示等待元素判断元素是否存在于dom

        :param selector:
        :param timeout: 显示等待超时时长
        :param poll_frequency: 检测的间隔步长，默认为0.5s
        :return:
        """
        by = selector[0]
        value = selector[1]
        element = None
        if by in ByType.get_member_values():
            try:
                if by == ByType.ID:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.ID, value)))
                elif by == ByType.NAME:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.NAME, value)))
                elif by == ByType.CLASS_NAME:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.CLASS_NAME, value)))
                elif by == ByType.TAG_NAME:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.TAG_NAME, value)))
                elif by == ByType.LINK_TEXT:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.LINK_TEXT, value)))
                elif by == ByType.PARTIAL_LINK_TEXT:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
                elif by == ByType.CSS_SELECTOR:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                elif by == ByType.XPATH:
                    element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.presence_of_element_located((By.XPATH, value)))
            except NoSuchElementException as e:
                log.error("❌ {}: {}".format(value, e.msg))
                raise e
            else:
                return element
        else:
            raise ValueError('❌ by value error, please use: %s' % ByType.get_member_values())

    def send_keys(self, input_box_selector: list, value):
        """
        输入框操作

        :param input_box_selector: 输入框定位
        :param value: 输入值
        :return:
        """
        _input = self.find_element(input_box_selector)
        try:
            _input.clear()
            _input.send_keys(value)
        except Exception as e:
            log.error('❌ Input value error %s' % e)
            raise e
        else:
            log.info('Input value %s' % value)

    def jscript(self, js):
        """
        执行js脚本

        :param js: js代码
        :return:
        """
        try:
            self.driver.execute_script(js)
        except Exception as e:
            log.error('❌ Execute js error %s' % e)
            raise e
        else:
            log.info('Execute js %s' % js)

    def save_screenshot(self, filename):
        """
        保存截图

        - 格式要求: *fail*.png / *pass*.png, 文件名中必须包含 fail 或 pass 字段

        :param filename: 图片文件名
        :return:
        """
        list_value = []
        _list = filename.split('.')
        for value in _list:
            list_value.append(value)
        if list_value[1] == 'png':
            if not os.path.exists(path_conf.FAIL_IMG_PATH):
                os.makedirs(path_conf.FAIL_IMG_PATH)
            if not os.path.exists(path_conf.PASS_IMG_PATH):
                os.makedirs(path_conf.PASS_IMG_PATH)
            try:
                if 'fail' in list_value[0]:
                    self.driver.save_screenshot(os.path.join(path_conf.FAIL_IMG_PATH, filename))
                elif 'pass' in list_value[0]:
                    self.driver.save_screenshot(os.path.join(path_conf.PASS_IMG_PATH, filename))
                else:
                    log.error('❌ Failed to save screenshot, please use "fail" or "pass" in the file name')
            except Exception as e:
                log.error('❌ Save screenshot error %s! %s' % filename, e)
                raise e
            else:
                print('Screenshot:', filename)  # 进行打印识别，为了触发保存图片到测试报告
                log.info('Screenshot was saved successfully')
        else:
            log.error('❌ Failed to save screenshot, please use the "png" format')

    def alert_accept(self):
        """
        确认错误警告弹窗

        :return:
        """
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            log.error('❌ Confirm the warning popup error %s' % e)
            raise e
        else:
            log.info('Confirm the warning popup')

    def alert_dismiss(self):
        """
        取消警告框

        :return:
        """
        try:
            self.driver.switch_to.alert.dismiss()
        except Exception as e:
            log.error('❌ Cancel the warning popup error %s' % e)
            raise e
        else:
            log.info('Cancel the warning popup')

    def forward(self):
        """
        浏览器前进操作

        :return:
        """
        try:
            self.driver.forward()
        except Exception as e:
            log.error("❌ Page click forward error %s" % e)
            raise e
        else:
            log.info("Page click forward")

    def back(self):
        """
        浏览器后退操作

        :return:
        """
        try:
            self.driver.back()
        except Exception as e:
            log.error('❌ Page click back error %s' % e)
            raise e
        else:
            log.info("Page click back")

    def f5(self):
        """
        刷新界面

        :return:
        """
        try:
            self.driver.refresh()
        except Exception as e:
            log.error('❌ Refresh page error %s' % e)
            raise e
        else:
            log.info('Refresh page')

    def refresh(self):
        self.f5()

    def set_window_size(self, width, height):
        """
        设置浏览器窗口大小

        :param width:
        :param height:
        :return:
        """
        try:
            self.driver.set_window_size(width, height)
        except Exception as e:
            log.error('❌ Set current window size error %s' % e)
            raise e
        else:
            log.info(f'Set current window size {width}x{height}')

    def get_window_size(self):
        """
        获取当前窗口大小

        :return:
        """
        try:
            size = self.driver.get_window_size()
        except Exception as e:
            log.error('❌ Get current window size error %s' % e)
            raise e
        else:
            log.info('Get current window size %s' % size)
            return size

    def max_window(self):
        """
        最大化窗口

        :return:
        """
        try:
            self.driver.maximize_window()
        except Exception as e:
            log.error('❌ Maximize the window error %s' % e)
            raise e
        else:
            log.info('Maximize the window')

    @staticmethod
    def get_attribute_content(selector_expression, gtr='textContent') -> str:
        """
        获取元素/隐藏元素的 text 值：

        - get_attribute('textContent') 获取元素标签的内容
        - get_attribute('innerHTML') 获取元素内的全部HTML
        - get_attribute('outerHTML')  获取包含选中元素的HTML

        :param selector_expression: 元素定位表达式, 建议使用上文已封装的定位方式
        :param gtr: 定义获取内容
        :return:
        """
        try:
            content = str(selector_expression.get_attribute(gtr))
        except Exception as e:
            log.error('❌ Get attribute %s error %s' % (gtr, e))
            raise e
        else:
            log.info('Get attribute %s value %s' % (gtr, content))
            return content

    @staticmethod
    def get_attribute(selector_expression, element: str) -> str:
        """
        获取指定元素value

        :param selector_expression: 元素定位表达式, 建议使用上文已封装的定位方式
        :param element: 指定元素
        :return:
        """
        try:
            text = selector_expression.get_attribute(element)
        except Exception as e:
            log.error('❌ Get attribute %s error %s' % (element, e))
            raise e
        else:
            log.info('Get attribute %s value %s' % (element, text))
            return text

    def get_title(self) -> str:
        """
        获取链接title

        :return:
        """
        title = self.driver.title
        log.info('Get current window title %s' % title)
        return title

    def click(self, selector: list):
        """
        点击元素

        :param selector: 元素定位, example: ['id', 'kw']
        :return:
        """
        try:
            self.find_element(selector).click()
        except BaseException as e:
            display = self.element_wait(selector)
            if display:
                self.find_element(selector).click()
                log.info('Click the element %s' % selector)
            else:
                log.error(f'❌ Click the element {selector} error {e}')
                raise e
        else:
            log.info('Click the element %s' % selector)

    def right_click(self, selector):
        """
        右击元素

        :param selector: 元素定位, example: ['id', 'kw']
        :return:
        """
        try:
            ele = self.find_element(selector)
            ActionChains(self.driver).context_click(ele).perform()
            log.info('Right click element')
        except Exception as e:
            log.error('❌ Right click element error %s' % e)
            raise e

    def double_click(self, selector):
        """
        双击元素

        :param selector: 元素定位, example: ['id', 'kw']
        :return:
        """
        try:
            ele = self.find_element(selector)
            ActionChains(self.driver).double_click(ele).perform()
        except Exception as e:
            log.error('❌ Double click element error %s' % e)
            raise e
        else:
            log.info('Double click element')

    def click_left_xy(self, x, y, double_click=False):
        """
        点击页面指定 X,Y 坐标

        :param x: x坐标
        :param y: y坐标
        :param double_click: 左键点击次数
        """
        if not double_click:
            try:
                ActionChains(self.driver).move_by_offset(x, y).click().perform()
            except Exception as e:
                log.error(f'❌ Left mouse button clicked coordinate ({x},{y}) error %s' % e)  # noqa: E501
                raise e
            else:
                log.info('Left mouse button clicked coordinate (%s,%s)' % (x, y))
        else:
            try:
                ActionChains(self.driver).move_by_offset(x, y).double_click().perform()
            except Exception as e:
                log.error(f'❌ Left mouse button clicked coordinate ({x},{y}) error %s' % e)  # noqa: E501
                raise e
            else:
                log.info('Left mouse button clicked coordinate (%s,%s)' % (x, y))
        # 将鼠标位置恢复到移动前
        ActionChains(self.driver).move_by_offset(-x, -y).perform()

    def click_right_xy(self, x, y):
        """
        点击页面指定 X,Y 坐标

        :param x: x坐标
        :param y: y坐标
        """
        try:
            ActionChains(self.driver).move_by_offset(x, y).context_click().perform()
        except Exception as e:
            log.error(f'❌ Right mouse button clicked coordinate ({x},{y}) error %s' % e)  # noqa: E501
            raise e
        else:
            log.info('Right mouse button clicked coordinate (%s,%s)' % (x, y))
        ActionChains(self.driver).move_by_offset(-x, -y).perform()

    def hover(self, selector):
        """
        鼠标悬停操作

        :param selector:
        :return:
        """
        try:
            element = self.find_element(selector)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            log.error('❌ Mouse hover error %s' % e)
            raise e
        else:
            log.info('Mouse hover {}'.format(selector))

    def current_window_handle(self) -> str:
        """
        获取当前页面句柄

        :return:
        """
        try:
            handle = self.driver.current_window_handle
        except Exception as e:
            log.error('❌ Get the current handle error %s' % e)
            raise e
        else:
            log.info('Get the current handle %s' % handle)
            return handle

    def current_window_handles(self) -> list:
        """
        获取所有窗口句柄

        :return:
        """
        try:
            handles = self.driver.window_handles
        except Exception as e:
            log.error('❌ Get all handles error %s' % e)
            raise e
        else:
            log.info('Get all handles %s' % handles)
            return handles

    def switch_to_new_window(self):
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 3:
                    break
            self.driver.switch_to.window(all_handle[-1])
        except Exception as e:
            log.error('❌ Switch to new window error %s' % e)
            raise e
        else:
            log.info(f'Switch to new window {self.driver.current_url}')

    def drag(self, start, end):  # frame,
        """
        页面元素拖动至目标元素

        :param start: 起步元素定位
        :param end: 目标元素定位
        """
        try:
            start = self.find_element(start)
            end = self.find_element(end)
            ActionChains(self.driver).drag_and_drop(start, end).perform()
        except Exception as e:
            log.error('❌ Drag and drop element error %s' % e)
            raise e
        else:
            log.info('Drag and drop element')
