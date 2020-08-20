import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sendEmail = "jsh1938@gmail.com"
recvEmail = "jsh1400512@naver.com"
password = "input password"

smtpName = "smtp.gmail.com"
smtpPort = 587

msg = MIMEMultipart()

msg['Subject'] = "메일 제목"
msg['from'] = sendEmail
msg['to'] = recvEmail

text = "메일 내용"
contentpart = MIMEText(text)
msg.attach(contentpart)

etcFileName = '소마.png'
with open(etcFileName, 'rb') as etcFD :
    etcPart = MIMEApplication(etcFD.read())
    etcPart.add_header('Content-Disposition', 'attachment', filename=etcFileName)
    msg.attach(etcPart)

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()
