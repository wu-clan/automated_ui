import smtplib

from XTestRunner import HTMLTestRunner

from po.common.log import log
from po.core import get_conf


def send_email_report(filename: str):
    try:
        HTMLTestRunner.send_email(
            to=get_conf.EMAIL_SEND_TO,
            user=get_conf.EMAIL_USER,
            password=get_conf.EMAIL_PASSWORD,
            host=get_conf.EMAIL_SERVER,
            port=get_conf.EMAIL_PORT,
            ssl=get_conf.EMAIL_SSL,
            subject=get_conf.PROJECT + '_testreport',
            attachments=filename
        )
    except smtplib.SMTPException as e:
        log.error(f'❌ Email report send error: {e}')
        raise e
    else:
        log.info('✅ Email report send successfully')
