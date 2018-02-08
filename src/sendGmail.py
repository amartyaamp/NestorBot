#!/usr/bin/env python
"""This script send a mail to recipient which is provided by user"""


import smtplib

from settings import email, password


class Mail(object):

    def __init__(self, recipient, subject="", body=""):

        # defining all the variables
        self.gmail_user = email
        self.gmail_pwd = password
        self.from_user = email      
        self.to_user = recipient if isinstance(recipient, list) else [recipient]  # Handles list also
        self.subject = subject
        self.text = body

        # Prepare actual message
        self.message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                       """ % (self.from_user, ", ".join(self.to_user), self.subject, self.text)

    def send_email(self):

        """Utility function to send mail
           using smtplib method.

        Parameters
        ----------
        recipient: list or str
            Email Id of person whom message to be sent.
        subject : str
            Subject line for the message.
        body : str
            All the message/information which is to be sent.

        Returns `True` if mail sent successfully,
           `False` otherwise.

        """

        try:
            # creates SMTP session
            server = smtplib.SMTP("smtp.gmail.com", 587)

            # Identify yourself to an ESMTP server using EHLO
            server.ehlo()

            # start TLS to handle security
            server.starttls()

            # Authentication
            server.login(self.gmail_user, self.gmail_pwd)

            # sending the mail
            server.sendmail(self.from_user, self.to_user, self.message)

            print('successfully sent the mail to {}'.format(self.to_user))

            return True

        # Handling all the possible exception
        except smtplib.SMTPHeloError:

            print('The server did not responded properly, please try again')
            return False

        except smtplib.SMTPAuthenticationError:

            print('Your account name or password is incorrect, please try again')
            return False

        except smtplib.SMTPException as e:

            print("Could not send the emails: %s" % e)
            return False

        finally:

            # Terminate the SMTP session
            server.quit()
