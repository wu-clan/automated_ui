import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from po.common.log import log
from po.core import get_conf
from po.core.path_conf import REPORT_PATH


class SendMail:

    def __init__(self, filename: str):
        self.filename = filename

    def take_messages(self):
        """生成邮件的内容，和html报告附件"""
        msg = MIMEMultipart()
        msg['Subject'] = get_conf.REPORT_DESCRIPTION
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 读取要发送的附件
        with open(os.path.join(REPORT_PATH, self.filename), 'rb') as f:
            mail_body = str(f.read())

        # 邮件正文
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(html)

        # 邮件附件
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = f'attachment; filename={self.filename}'
        msg.attach(att1)

        return msg

    def send(self):
        """发送邮件"""
        try:
            if get_conf.EMAIL_SSL:
                smtp = smtplib.SMTP_SSL(host=get_conf.EMAIL_SERVER, port=get_conf.EMAIL_PORT)
            else:
                smtp = smtplib.SMTP(host=get_conf.EMAIL_SERVER, port=get_conf.EMAIL_PORT)
            smtp.login(get_conf.EMAIL_USER, get_conf.EMAIL_PASSWORD)
            smtp.sendmail(get_conf.EMAIL_USER, get_conf.EMAIL_SEND_TO, self.take_messages().as_string())
            smtp.quit()
        except Exception as e:
            log.error(f'测试报告邮件发送失败: \n {e}')
        else:
            log.success("测试报告邮件发送成功")
