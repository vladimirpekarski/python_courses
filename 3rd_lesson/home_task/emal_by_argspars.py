# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse
import smtplib
import sys

from email.message import Message
from email.header import Header


def parse_args():
    parser = argparse.ArgumentParser(description='Script for sending emails')
    parser.add_argument('-s', help='Email subject', required=True)
    parser.add_argument('-m', help='Email message', required=True)
    parser.add_argument('-e_f', help='Email From', required=True)
    parser.add_argument('-e_t', help='Email To', required=True)
    parser.add_argument('-smtp', help='Smtp server, default: smtp.gmail.com',
                        default='smtp.gmail.com')
    parser.add_argument('-smtp_port', help='Smtp server port, default: 587',
                        type=int, default='587')
    parser.add_argument('-user', help='User', required=True)
    parser.add_argument('-u_pass', help='User password', required=True)
    return parser.parse_args()


def sent_message(args):
    msg = Message()
    header = Header(args['header'].decode('cp1251'), 'utf-8')
    msg['Subject'] = header
    text = args['message'].decode('cp1251')
    msg.set_payload(text.encode('utf-8'))
    smpt_obj = smtplib.SMTP(args['smtp'], args['smtp_port'])
    smpt_obj.ehlo()
    smpt_obj.starttls()
    smpt_obj.login(args['user'], args['user_pass'])
    error_emails = smpt_obj.sendmail(args['email_from'], args['email_to'],
                                     msg.as_string())
    smpt_obj.quit()

    return error_emails


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please use -h key to how to use script")
    else:
        args = parse_args()
        args_for_emai = {'header': args.s,
                         'message': args.m,
                         'smtp': args.smtp,
                         'smtp_port': args.smtp_port,
                         'user': args.user,
                         'user_pass': args.u_pass,
                         'email_from': args.e_f,
                         'email_to': args.e_t,
                         }
        error_email = sent_message(args_for_emai)
        if not error_email:
            print("Email has been successfully sent")
        else:
            print('Email to {} hasn\'t been sent'.format(error_email))
