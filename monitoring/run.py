import argparse
import os
import smtplib
from datetime import datetime
from time import strftime

import requests
from monitoring.config import CHECKS, EMAILS, DIR
from monitoring.utils import sendmail, top, ps, netstat

parser = argparse.ArgumentParser()
args = parser.parse_args()

msg = ''

dirname = os.path.join(DIR, datetime.utcnow().strftime('%Y_%m_%d_%H_%M'))
os.makedirs(dirname, exist_ok=True)

for url, checks in CHECKS.items():
    url_msg = ''

    response = requests.get(url)
    for check in checks:
        if not check.do(response):
            error_str = check.error2str(url, response)
            url_msg += error_str + '\n'

    if url_msg:
        msg += '\n\n{}\n'.format(url) + url_msg

if EMAILS and msg:
    smtp = smtplib.SMTP('localhost', 1025)
    for email in EMAILS:
        sendmail(smtp, email, msg + '\n\n' + dirname)

    smtp.close()

if msg:
    with open(os.path.join(dirname, 'log.log'), 'w') as f:
        f.write(msg)

    top(os.path.join(dirname, 'top.log'))
    ps(os.path.join(dirname, 'ps.log'))
    netstat(os.path.join(dirname, 'ps.log'))
