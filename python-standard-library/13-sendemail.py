from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.imae import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Goh Sheen An"
message["to"] = "sheen.an.goh@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("test.png").read_bytes())

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("example@gmail.com", "example passwords")
    smtp.send_messsage(message)
    print("sent...")
