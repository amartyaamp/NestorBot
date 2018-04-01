# Created: 04-02-2018
# Author: Shankar Jha
# Based on code from examples at: https://developers.google.com/gmail/api/


from __future__ import print_function
import os
import base64
import email.mime.text
import httplib2
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.discovery import build
from apiclient import errors
from constants import *

# --------------------------------------------------------------------------------------
# This is the name of the secret file you download from https://console.developers.google.com/iam-admin/projects
CLIENT_SECRET_FILE = 'client_secret.json'

# File will be automatically created in ~/.credentials holding your credentials.
# this is the first time authentication, mean you don't have to re-authenticate each time you connect to the API.
# Give it a unique name
# keep this file in safe place, don't share this with anyone
CREDENTIAL_FILE = 'nestorbot_gmail.json'

APPLICATION_NAME = 'NestorBot'
# Set to True if you want to authenticate manually
# Set to False if you want to authenticate via browser redirect.
MANUAL_AUTH = True
# --------------------------------------------------------------------------------------

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    if MANUAL_AUTH:
        flags.noauth_local_webserver=True
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials at ~/.credentials/gmail-python-quickstart.json
SCOPES = ['https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.compose',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.send']


class Gmail():
    """ This class send mail to recipient using Gmail API """

    def send_mail(self, recipient_address, subject, body):
        print('Sending your message, please wait...')
        try:
            message = self.__create_message(SOURCE_GMAIL, recipient_address, subject, body)
            
            credentials = self.get_credentials() # obtains credential from store
            service = self.__build_service(credentials)
            raw = message['raw']
            raw_decoded = raw.decode("utf-8")
            message = {'raw': raw_decoded}
            message_id = self.__send_message(service, 'me', message)
            if message_id:
                print('Message sent successfully to : ' + recipient_address)
            else:
                print("Please provide your correct information")
            return message_id
        except TypeError:
            print("Please give your information correctly")
            return message_id

    def get_credentials(self):
        """Get valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
         Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       CREDENTIAL_FILE)

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
              os.path.join(CLIENT_SECRET_PATH, CLIENT_SECRET_FILE), SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:# Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials




    def __create_message(self, sender, to, subject, message_text):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
      Returns:
        An object containing a base64url encoded email object.
      """
      message = email.mime.text.MIMEText(message_text, 'plain', 'utf-8')
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      encoded_message = {'raw': base64.urlsafe_b64encode(message.as_bytes())}
      return encoded_message


   
    def __send_message(self, service, user_id, message):
      """Send an email message.
      Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.
      Returns:
        Sent Message ID.
      """
      try:
          message = (service.users().messages().send(userId=user_id, body=message)
                    .execute())
          return message['id']

      except errors.HttpError as error:
          
          print ('An error occurred: %s' % error)

    def __build_service(self, credentials):
        """Build a Gmail service object.

        Args:
            credentials: OAuth 2.0 credentials.
        Returns:
            Gmail service object.
        """
        http = httplib2.Http()
        http = credentials.authorize(http)
        return build('gmail', 'v1', http=http)


def main():
  #A = Gmail()
  #A.get_credentials()


  to_address = input("enter recipient address: ")
  subject = input("enter subject: ")
  body = input("enter body: ")

  Gmail().send_mail(to_address, subject, body)


if __name__ == "__main__":
  main()