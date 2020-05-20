from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.imae import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Goh Sheen An"
message["to"] = "sheen.an.goh@gmail.com"
message["subject"] = "This is a test"

body = template.substitute({"name": "John"})

message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("test.png").read_bytes())

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("example@gmail.com", "example passwords")
    smtp.send_messsage(message)
    print("sent...")
