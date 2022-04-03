#!/usr/bin/python3# -*- coding: utf-8 -*-# @Time    : 2021/2/3 11:04# @Author  : wu# @Software: PyCharmimport win32conimport win32guifrom selenium import webdriverfrom po.common.log import logdef file_operations(filePath, browser_type="chrome"):    """    ******《上传文件》《导出文件》 Windows 窗口 ******    :param filePath: 传入文件路径 绝对路径 包括文件名称    :param browser_type: 浏览器默认 chrome    """    # 判断浏览器title，不同的浏览器上传的 title(标题头) 不一样    if browser_type == "chrome":        title = "打开" or "另存为"    else:        title = ""    dialog = win32gui.FindWindow("#32770", title)    if title == "打开":        try:            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)            # 编辑按钮            Edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)            # 往编辑当中，输入文件路径            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)            # 打开按钮            button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(O)")            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮        except Exception as e:            log.error('打开文件 {0} 错误'.format(filePath))            raise e        else:            log.info('打开文件 {0} 成功'.format(filePath))    elif title == "另存为":        try:            DUIViewWndClassName = win32gui.FindWindowEx(dialog, 0, "DUIViewWndClassName", None)            DirectUIHWND = win32gui.FindWindowEx(DUIViewWndClassName, 0, "DirectUIHWND", None)            FloatNotifySink = win32gui.FindWindowEx(DirectUIHWND, 0, "FloatNotifySink", None)            ComboBox = win32gui.FindWindowEx(FloatNotifySink, 0, "ComboBox", None)            # 编辑存储路径            Edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)            # 往编辑当中，输入文件路径            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)            # 保存按钮            button = win32gui.FindWindowEx(dialog, 0, "Button", "保存(S)")            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击保存按钮        except Exception as e:            log.error('另存为文件 {0} 错误'.format(filePath))            raise e        else:            log.info('另存为文件 {0} 成功'.format(filePath))    else:        print("请查看windows窗口title信息是否为：打开或另存为.")if __name__ == '__main__':    dr = webdriver.Chrome()    dr.get('https://airportal.cn/')    dr.find_element_by_id('send').click()    try:        file_operations(r'D:\testdata\相机信息.xlsx')    except Exception as e:        raise e    else:        print('success')    dr.close()