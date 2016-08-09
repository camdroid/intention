import smtplib
import secrets

from_addr = secrets.from_addr
to_addr = secrets.to_addr
smtp_server = secrets.smtp_server

s = smtplib.SMTP(smtp_server)
s.starttls()
s.login(from_addr, secrets.email_password)
msg = 'From: {from_addr}\r\nTo: {to_addr}\r\n\r\nHello World!\r\n'.format(from_addr=from_addr, to_addr=to_addr)
            
ret = s.sendmail(from_addr, to_addr, msg)
s.quit()
