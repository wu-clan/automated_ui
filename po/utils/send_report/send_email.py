import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from po.common.log import log
from po.core import get_conf


class SendMail:

    def __init__(self, filename: str):
        self.filename = filename

    def take_messages(self):
        """生成邮件的内容，和html报告附件"""
        msg = MIMEMultipart()
        msg['Subject'] = get_conf.REPORT_DESCRIPTION
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        msg['From'] = get_conf.REPORT_TESTER

        # 邮件正文
        html = MIMEText('<h1>自动化测试报告</h1>', _subtype='html', _charset='utf-8')
        msg.attach(html)

        # 邮件附件
        att = MIMEText(str(open(self.filename, 'rb').read()), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=f'{Path(self.filename).name}')
        msg.attach(att)

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
            log.error(f'❌ Test report email send: {e}')
        else:
            log.success("Test report email send success")
