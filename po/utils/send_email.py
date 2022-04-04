#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from po.common.log import log
from po.core import get_conf, path_conf


class SendMail:
    def __init__(self, address=None):
        """
        邮件接收地址

        :param address: list or str
        """
        if address is None:
            self.send_to = get_conf.EMAIL_SEND_TO
        else:
            self.send_to = address

    @staticmethod
    def __get_report():
        """ 获取最新测试报告 """
        dirs = os.listdir(path_conf.REPORT_PATH)
        dirs.sort()
        # 取最后一个
        report = dirs[-1]
        # print('The report name is: {0}'.format(report))
        return report

    def __take_messages(self):
        """ 生成邮件的内容，和html报告附件 """
        new_report = self.__get_report()
        self.msg = MIMEMultipart()

        self.msg['Subject'] = path_conf.PROJECT_NAME + '自动测试报告'  # 主题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(path_conf.REPORT_PATH, new_report), 'rb') as f:
            mail_body = f.read()
        # html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # self.msg.attach(html)
        html = MIMEText('HTML 测试报告', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """ 发送邮件 """
        self.__take_messages()
        self.msg['from'] = get_conf.EMAIL_USER
        try:
            smtp = smtplib.SMTP(get_conf.EMAIL_HOST_SERVER, get_conf.EMAIL_PORT)
            smtp.login(get_conf.EMAIL_USER, get_conf.EMAIL_PASSWORD)
            smtp.sendmail(self.msg['from'], self.send_to, self.msg.as_string())
        except Exception as e:
            log.error('Error: Failed to send email \n {}', e)
            raise
        else:
            smtp.close()
            log.success("Success: Send test report email successfully")


send_mail = SendMail()

if __name__ == '__main__':
    send_mail.send()
