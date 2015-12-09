# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse
import smtplib

from email.message import Message
from email.header import Header


def parse_args():
    parser = argparse.ArgumentParser(description='Script for sending emails')
    parser.add_argument('-s', '--subject',help='Email subject',
                        required=True)
    parser.add_argument('-m', '--message', help='Email message',
                        required=True)
    parser.add_argument('-e_f', '--email-from', help='Email From',
                        required=True)
    parser.add_argument('-e_t', '--email-to', help='Email To',
                        required=True)
    parser.add_argument('-smtp', '--smpt-host', help='Smtp server, default: smtp.gmail.com',
                        default='smtp.gmail.com')
    parser.add_argument('-s_port', '--smpt-port', help='Smtp server port, default: 587',
                        type=int, default='587')
    parser.add_argument('-u', '--user', help='User', required=True)
    parser.add_argument('-u_p', '--user-pass', help='User password',
                        required=True)
    return parser.parse_args()


def send_message(args):
    msg = Message()
    header = Header(args.subject.decode('cp1251'), 'utf-8')
    msg['Subject'] = header
    text = args.message.decode('cp1251')
    msg.set_payload(text.encode('utf-8'))
    smpt_obj = smtplib.SMTP(args.smpt_host, args.smpt_port)
    smpt_obj.ehlo()
    smpt_obj.starttls()
    smpt_obj.login(args.user, args.user_pass)
    error_emails = smpt_obj.sendmail(args.email_from, args.email_to,
                                     msg.as_string())
    smpt_obj.quit()

    return error_emails


if __name__ == '__main__':
    args = parse_args()
    error_email = send_message(args)
    if not error_email:
        print("Email has been successfully sent")
    else:
        print('Email to {} hasn\'t been sent'.format(error_email))
