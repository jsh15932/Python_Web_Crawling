import smtplib
from email.mime.text import MIMEText

sendEmail = "jsh1400512@naver.com"
recvEmail = "jsh1938@gmail.com"
password = "input password"

smtpName = "smtp.naver.com"
smtpPort = 587

text = "메일 내용"
msg = MIMEText(text)

msg['Subject'] = "메일 제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string())

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()