"""this program is to automate email process using hotmail"""
import smtplib

user       = 'your_email_address'
password   = 'your_password'
from_email = 'sender_address@mail.com'
to_email   = 'recipient_address@mail.com'
smtp_obj   = smtplib.SMTP('smtp.live.com',587) #using hotmail as an example

smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(user,password)
smtp_obj.sendmail(from_email,to_email,'Subject: Subject\nHello world,\nThis is the message.\nsender')
smtp_obj.quit()



