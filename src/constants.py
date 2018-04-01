import os

#SMTP details for Outlook
SMTP_SERVER_OUTLOOK = "smtp-mail.outlook.com"
SMTP_SERVER_PORT_OUTLOOK = 587

#Source mail authentication details

SOURCE_MAIL = os.environ["SOURCE_MAIL"]
SOURCE_PASSWORD = os.environ["SOURCE_PASSWORD"]

#LUIS Specifications
LUIS_APP_KEY = os.environ['LUIS_APP_KEY']
LUIS_API_SUBSCRIPTION = os.environ['LUIS_API_SUBSCRIPTION']

# For the gmail API

CLIENT_SECRET_PATH = os.environ['CLIENT_SECRET_PATH']
SOURCE_GMAIL = os.environ['SOURCE_GMAIL']

