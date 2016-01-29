#!/usr/bin/python

#This script sends an email from lewis.peaty@gmail.com to robot@derpen.com
#It could be further parametrised to take a custom destination, but the sender (smtp server) is best hard coded
#because it's a bitch to get the details right. Gmail seems to be much friendlier than derpen in this regard.
#Also robot@derpen.com mysteriously filters mail sent from this computer and not gmail (possibly outgoing ports are #blocked?).

import smtplib
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-t")
parser.add_argument("-f")
parser.add_argument("-m")
parser.add_argument("-s")
args = parser.parse_args()
if args.verbose:
   print "verbosity turned on"
to = 'robot@derpen.com'
if args.f:
	frm = args.f
else:
	frm = 'lewis.peaty@gmail.com'
gmail_user = 'lewis.peaty@gmail.com'
gmail_pwd = 'hlthttdqwgicceqy'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + frm + '\n' + 'Subject: ' + args.s + '\n'
msg = header + args.m
print msg
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()
