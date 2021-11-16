import yagmail
import json

with open('config.json', 'r') as f:
    config = json.load(f)
 
sender = config['sender']
sender_pw = config['password']
receiver = 'dtbarnett@suddenlink.net'
subject = 'Test subject'
content = ["""This is the content for the test email application""", 'text.txt']

yag = yagmail.SMTP(user=sender, password=sender_pw)
yag.send(to=receiver, subject=subject, contents=content)
print('email sent')