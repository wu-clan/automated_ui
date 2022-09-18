#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from po.common.log import log
from po.core import path_conf, get_conf


class BasePage(object):

    def __init__(self, driver, url=get_conf.MAIN_PATH):
        """
        初始化驱动信息和测试主入口

        :param driver:
        :param url:
        """
        self.driver = driver
        self.base_url = url

    def _open(self, url: str):
        try:
            self.driver.get(url)
            # 打开url隐式等待10秒钟
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.exception(e)
            raise ValueError('❌ %s Address access error, Please check！' % url)

    def open(self):
        """
        打开程序主入口

        :return:
        """
        self._open(self.base_url)
        log.info('%s > > Loading succeeded!' % self.base_url)
        return self.base_url

    def find_element_wait(self, *locator, timeout=5, poll_frequency=0.5):
        """
        显示等待查找给定 By 策略和定位器的元素,元素必须为非隐藏,可能时首选

        - example: find_element_wait(By.XPATH, 'kw')

        :param timeout: 显示等待超时时长
        :param poll_frequency: 检测的间隔步长，默认为0.5s
        :return:
        """
        try:
            # 显示等待查找元素
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.visibility_of_element_located(locator))
        except NoSuchElementException as e:
            log.error('❌ find element timeout in %ss: %s', timeout, e)
            raise e
        else:
            return self.driver.find_element(*locator)

    def find_elements_wait(self, *locator, timeout=5, poll_frequency=0.5):
        """
        显示等待查找给定 By 策略和定位器的多个元素,元素必须为非隐藏,可能时首选

        - example: find_elements_wait(By.XPATH, 'kw')

        :param timeout: 显示等待超时时长
        :param poll_frequency: 检测的间隔步长，默认为0.5s
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.visibility_of_element_located(locator))
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
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.presence_of_element_located(*locator))
        except Exception:  # noqa
            return False
        else:
            return True

    def find_element(self, selector: list):
        """
        定位元素

        :param selector: 定位方式及定位表达式, example: ['id', 'kw']
        :return:
        """
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
            except NoSuchElementException as e:
                log.error("❌ {}: {}".format(value, e.msg))
                raise e
            else:
                return element
        else:
            raise ValueError('❌ by error, only these "id, name, class, tag, link, plink, css, xpath" of one')

    def find_elements(self, selector: list):
        """
        定位多个元素

        :param selector: 定位方式及定位表达式, example: ['id', 'kw']
        :return:
        """
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            try:
                if by == 'id':
                    element = self.driver.find_elements_by_id(value)
                elif by == 'name':
                    element = self.driver.find_elements_by_name(value)
                elif by == 'class':
                    element = self.driver.find_elements_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_elements_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_elements_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_elements_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_elements_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_elements_by_xpath(value)
            except NoSuchElementException as e:
                log.error("❌ {}: {}".format(value, e.msg))
                raise e
            else:
                return element
        else:
            raise ValueError('❌ by error, only these "id, name, class, tag, link, plink, css, xpath" of one')

    def element_wait(self, selector: list):
        """
        显示等待元素判断元素是否存在于dom

        :param selector:
        :return:
        """
        by = selector[0]
        value = selector[1]
        if by in ['id', 'name', 'class', 'link_text', 'css', 'xpath']:
            messages = '❌ element {0} not find in{1}S.'.format(selector, 5)
            try:
                if by == "id":
                    WebDriverWait(self.driver, 5, 1).until(ec.presence_of_element_located((By.ID, value)), messages)
                elif by == "name":
                    WebDriverWait(self.driver, 5, 1).until(ec.presence_of_element_located((By.NAME, value)), messages)
                elif by == "class":
                    WebDriverWait(self.driver, 5, 1).until(ec.presence_of_element_located((By.CLASS_NAME, value)),
                                                           messages)
                elif by == "link_text":
                    WebDriverWait(self.driver, 5, 1).until(ec.presence_of_element_located((By.LINK_TEXT, value)),
                                                           messages)
                elif by == "xpath":
                    WebDriverWait(self.driver, 5, 1).until(ec.presence_of_element_located((By.XPATH, value)), messages)
                elif by == "css":
                    WebDriverWait(self.driver, 5, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, value)),
                                                           messages)
            except NoSuchElementException as e:
                log.error(messages)
                raise e
        else:
            raise ValueError('❌ by error, only these "id, name, class, link_text, css, xpath" of one')

    def send_keys(self, input_box: list, value):
        """
        输入框操作

        :param input_box: 输入框定位
        :param value: 输入值
        :return:
        """
        # 实例化inoutBox
        _input = self.find_element(input_box)
        try:
            _input.clear()
            _input.send_keys(value)
        except Exception as e:
            log.error('❌ input value: %s! %s' % value, e)
            raise e
        else:
            log.info('input value %s' % value)

    def jscript(self, js):
        """
        执行js脚本

        :param js: js代码
        :return:
        """
        try:
            self.driver.execute_script(js)
        except Exception as e:
            log.error('❌ execute js-script %s %s' % js, e)
            raise e
        else:
            log.info('execute js-script %s' % js)

    def save_screenshot(self, filename):
        """
        保存截图

        - 格式要求: r*fail*.png / r*pass*.png, 文件名中必须包含 fail 或 pass 字段

        :param filename: 图片文件名
        :return:
        """
        list_value = []
        _list = filename.split('.')  # 分割点
        for value in _list:
            list_value.append(value)
        if list_value[1] == 'png':
            if not os.path.exists(path_conf.FAIL_IMG_PATH):
                os.makedirs(path_conf.FAIL_IMG_PATH)
            if not os.path.exists(path_conf.PASS_IMG_PATH):
                os.makedirs(path_conf.PASS_IMG_PATH)
            if 'fail' in list_value[0]:
                try:
                    self.driver.save_screenshot(os.path.join(path_conf.FAIL_IMG_PATH, filename))
                except Exception as e:
                    log.error('❌ save screenshot %s! %s' % filename, e)
                    raise e
                else:
                    print('screenshot:', filename)  # 进行打印识别，为了触发保存图片到测试报告
                    log.info('[%s] screenshot was saved successfully' % filename)
            elif 'pass' in list_value[0]:
                try:
                    self.driver.save_screenshot(os.path.join(path_conf.PASS_IMG_PATH, filename))
                except Exception as e:
                    log.error('❌ save screenshot %s! %s' % filename, e)
                    raise e
                else:
                    print('screenshot:', filename)
                    log.info('[%s] screenshot was saved successfully' % filename)
            else:
                log.error('❌ [%s] failed to save, "fail" or "pass" not in filename')
        else:
            log.error('❌ [%s] failed to save，please use ".png"' % filename)

    def alert_accept(self):
        """
        确认错误警告弹窗

        :return:
        """
        try:
            alert = self.driver.switch_to.alert()
            alert.accept()  # 确认警告弹窗
        except Exception as e:
            log.error('❌ confirm warning popup %s' % e)
            raise e
        else:
            log.info('confirm warning popup')

    def alert_dismiss(self):
        """
        取消警告框

        :return:
        """
        try:
            self.driver.switch_to.alert.dismiss()
        except Exception as e:
            log.error('❌ cancel warning popup %s' % e)
            raise e
        else:
            log.info('cancel warning popup')

    def forward(self):
        """
        浏览器前进操作

        :return:
        """
        try:
            self.driver.forward()
        except Exception as e:
            log.error("❌ page click forward %s" % e)
            raise e
        else:
            log.info("page click forward")

    def back(self):
        """
        浏览器后退操作

        :return:
        """
        try:
            self.driver.back()
        except Exception as e:
            log.error('❌ page click back %s' % e)
            raise e
        else:
            log.info("page click back")

    def F5(self):
        """
        刷新界面

        :return:
        """
        try:
            self.driver.refresh()
        except Exception as e:
            log.error('❌ refresh page %s' % e)
            raise e
        else:
            log.info('refresh page')

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
            log.error('❌ set current window size！\n %s' % e)
            raise e
        else:
            log.info('set current window size %s x %s' % (width, height))

    def get_window_size(self):
        """
        获取当前窗口大小

        :return:
        """
        try:
            size = self.driver.get_window_size
        except Exception as e:
            log.error('❌ get the current window size %s' % e)
            raise e
        else:
            log.info('The current window size is %s' % size)
            return size

    def max_window(self):
        """
        最大化窗口

        :return:
        """
        try:
            self.driver.maximize_window()
        except Exception as e:
            log.error('❌ maximize the window！\n %s' % e)
            raise e
        else:
            log.info('maximize the window.')

    def get_attribute_customize(self, selector, gtr='textContent'):
        """
        获取元素/隐藏元素的 text 值：

        - get_attribute('textContent') 获取元素标签的内容
        - get_attribute('innerHTML') 获取元素内的全部HTML
        - get_attribute('outerHTML')  获取包含选中元素的HTML

        :param selector: 元素定位, 建议使用上文已封装的定位方式
        :param gtr: 定义获取内容
        :return:
        """
        try:
            t = str(selector.get_attribute(gtr))
        except Exception as e:
            log.error('❌ get_attribute %s text %s' % selector, e)
            raise e
        else:
            log.info('get_attribute text %s' % t)
            return t

    def get_attribute(self, selector, element: str):
        """
        获取指定元素value

        :param selector: 元素定位, 建议使用上文已封装的定位方式
        :param element: 指定元素
        :return:
        """
        try:
            t = selector.get_attribute(element)
        except Exception as e:
            log.error('❌ get_attribute %s value %s' % element, e)
            raise e
        else:
            log.info('get_attribute value %s' % t)
            return t

    def get_title(self):
        """
        获取链接title

        :return:
        """
        title = self.driver.title
        log.info('the title of the url is %s' % title)
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
                log.info('click the element %s' % selector)
            else:
                log.error(f'❌ click the element {e}')
                raise e
        else:
            log.info('click the element %s' % selector)

    def right_click(self, selector):
        """
        右击元素

        :param selector: 元素定位, example: ['id', 'kw']
        :return:
        """
        try:
            ele = self.find_element(selector)
            ActionChains(self.driver).context_click(ele).perform()
            log.info('right click element {}'.format(selector))
        except Exception as e:
            log.error('❌ right click element {}\n {}'.format(selector, e))
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
            log.error('❌ double click element {} {}'.format(selector, e))
            raise e
        else:
            log.info('double click element')

    def click_page_xy(self, x, y, click_left=True, click_number=1):
        """
        点击页面指定 X,Y 坐标

        :param x: x坐标
        :param y: y坐标
        :param click_left: 鼠标左键触发,如果为False,则默认鼠标右键点击
        :param click_number: 左键点击次数, 仅 1,2 可识别
        """
        if click_left and click_number:
            try:
                ActionChains(self.driver).move_by_offset(x, y).click().perform()
            except Exception as e:
                log.error(f'❌ left mouse button clicked coordinate ({x},{y}) %s' % e)
                raise e
            else:
                log.info('left mouse button clicked coordinate (%s,%s)' % (x, y))
        elif click_left and click_number == 2:
            try:
                ActionChains(self.driver).move_by_offset(x, y).double_click().perform()
            except Exception as e:
                log.error(f'❌ left mouse button clicked coordinate ({x},{y}) %s' % e)
                raise e
            else:
                log.info('left mouse button clicked coordinate (%s,%s)' % (x, y))
        else:
            try:
                ActionChains(self.driver).move_by_offset(x, y).context_click().perform()
            except Exception as e:
                log.error(f'❌ right mouse button clicked coordinate ({x},{y}) %s' % e)
                raise e
            else:
                log.info('right mouse button clicked coordinate (%s,%s)' % (x, y))
        ActionChains(self.driver).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

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
            log.error('❌ hover for element [%s] %s' % (selector, e))
            raise e
        else:
            log.info('hover for element [%s]' % selector)

    def current_window_handle(self):
        """
        获取当前页面句柄

        :return:
        """
        try:
            _handle = self.driver.current_window_handle
        except Exception as e:
            log.error('❌ get current handle error %s' % e)
            raise e
        else:
            log.info('Get the current handle [%s]' % _handle)
            return _handle

    def current_window_handles(self):
        """
        获取所有窗口句柄

        :return:
        """
        try:
            _handles = self.driver.window_handles
        except Exception as e:
            log.error('❌ get current all handles！\n %s' % e)
            raise e
        else:
            log.info('get current all handles %s' % _handles)
            return _handles

    # 切换至新窗口
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
            log.info('jump new window，new window url is -> {}'.format(self.driver.current_url))
        except Exception as e:
            log.error('❌ jump email_to new window {}'.format(e))
            raise e

    def drag(self, start, end):  # frame,
        """
        页面元素拖动至目标元素

        :param start: 起步元素定位
        :param end: 目标元素定位
        """
        try:
            # 起点
            start = self.find_element(start)
            # 终点
            end = self.find_element(end)
            ActionChains(self.driver).drag_and_drop(start, end).perform()
        except Exception as e:
            log.info('❌ drag element %s' % e)
        else:
            log.info('drag element')
