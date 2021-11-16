import yagmail
import os

sender = 'dantbarnett@gmail.com'
sender_pw = os.getenv('APP_PW')
receiver = 'dtbarnett@suddenlink.net'
subject = 'Test subject'
content = """This is the content for the test email application"""

yag = yagmail.SMTP(user=sender, password=sender_pw)
yag.send(to=receiver, subject=subject, contents=content)
print('email sent')
