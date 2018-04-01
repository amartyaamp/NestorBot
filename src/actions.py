from sendMail import send_mail, send_mail_gmail
from time import sleep
from message import Mail
"""
Failed attempt to create a table. Main pressure point was calling member functions using lambda.
Replacing with if-then logic for now.

action_items = {
	"send_mail": lambda: self.send_mail,
	"none": None,
	"wait_20": lambda: sleep(20) ,
	"store_body": lambda x: self.store_items(x, "body") ,
	"store_subj": lambda x: self.store_items(x, "subj"),
	"store_mailid": lambda x: self.store_items(x, "mailid")
}
"""

class Actions:

	def __init__(self):
		# set up an empty container of mails
		self.mail = Mail()

	def store_items(self, text, item_name):
		self.mail.__dict__[item_name] = text

	def send_mail(self):
		print ("[actionlog] - mailing to {} with sub - {} and {}".format(self.mail.mailid, self.mail.subj, self.mail.body))
		send_mail_gmail(self.mail.mailid, self.mail.subj, self.mail.body)

	
	def perform_action(self, action, text):

		#FIXME - change the ifelse to something else(table lookup maybe ?)
		if action == "send_mail":
			self.send_mail()
		elif action == "wait_20":
			sleep(20)
		elif action == "store_body":
			self.store_items(text, "body")
		elif action == "store_subj":
			self.store_items(text, "subj")
		elif action == "store_mailid":
			self.store_items(text, "mailid")