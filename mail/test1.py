import smtplib
from email.mime.text import MIMEText

sendEmail = "jsh1938@gmail.com"
recvEmail = "yoolee5526@naver.com"
password = "jsh!1400512"

smtpName = "smtp.gmail.com"
smtpPort = 587

text = "메일 내용"
msg = MIMEText(text)

msg['Subject'] = "메일 제목"
msg['From'] = sendEmail
msg['to'] = recvEmail
print(msg.as_string())

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()