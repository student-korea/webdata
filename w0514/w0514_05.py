import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "wnslove15"
password="7T4XWRX1ESWJ"
recvEmail = "wnslove15@naver.com"

text = "날씨정보 오늘날씨:맑음, 내일날씨:흐리고 비"
msg = MIMEText(text)
msg['Subject'] = "웹스크래핑 이메일 보내기"
msg['From'] = "wnslove15@naver.com"
msg['To']=recvEmail

s=smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("wnslove15",password)
s.sendmail("wnslove15@naver.com",recvEmail,msg.as_string())
s.close()