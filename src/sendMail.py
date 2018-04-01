import smtplib
from email.message import EmailMessage
from constants import *
from GmailSend import Gmail

"""
send_mail - simply send a message using the smtplib library
"""

def send_mail(recipient="", subject="", body=""):
	print ("Sending mail to ")
	print ("Recipient - {}".format(recipient))
	print ("Subject - {}".format(subject))
	print ("Body - {}".format(body))

	FROM = SOURCE_MAIL
	PASSWORD = SOURCE_PASSWORD
	TO = []
	TO.append(recipient)
	#Init server with the smtp server and port of your FROM id
	SERVER = SMTP_SERVER_OUTLOOK
	SERVER_PORT = SMTP_SERVER_PORT_OUTLOOK
	print("Initialization started..")
	server = smtplib.SMTP(SERVER, 25)
	server.connect(SERVER, SERVER_PORT)
	server.ehlo()
	server.starttls()
	server.ehlo()
	print(server.login(FROM, PASSWORD))
	print("server connected")
	msg = EmailMessage()
	msg["Subject"] = subject
	msg["To"] = TO
	msg["From"] = FROM
	msg.set_content(body)

	server.send_message(msg)
	print("Message sent!")

	server.quit()


def send_mail_gmail(recipient="", subject="", body=""):
	Gmail().send_mail(recipient, subject, body)

