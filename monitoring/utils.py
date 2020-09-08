import os
import smtplib
import subprocess
from email.mime.text import MIMEText
from subprocess import Popen, PIPE


def sendmail(smtp, email, msg):
    msg = MIMEText(msg)
    msg["From"] = "me@example.com"
    msg["To"] = email
    msg["Subject"] = ""

    smtp.sendmail("me@example.com", "email_address.ru", msg.as_string())


def top(filename, args=''):
    with open(filename, "w") as outfile:
        subprocess.call("top -b -n1 {}".format(args), shell=True, stdout=outfile)


def ps(filename):
    with open(filename, "w") as outfile:
        subprocess.call('ps aux', shell=True, stdout=outfile)


def netstat(filename):
    with open(filename, "w") as outfile:
        subprocess.call('netstat', shell=True, stdout=outfile)
