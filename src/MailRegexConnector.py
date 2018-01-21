from pybotframework.connector import Connector
import re
import json
import random
from sendMail import send_mail

"""
A connector for mail entities and intents
This uses regex  rules for intents and entities detection
"""

class MailRegexConnector(Connector):

    def __init__(self, intent_file, response_file):
        """
        Constructor.

        Parameters
        ----------
        model_file : str
            The file with the json dialog logic.

        """
        # state - 0, looks for intents and entities
        # state - 1, copy whatever text is given 

        self.state = 0 # to keep track of the state
        self.body = "" # placeholder for body of the mail
        self.subject = "" # placeholder for mail subject
        self.recipient = "" # placeholder for recipient, all three are used to shoot a mail


        self.intent_list = json.load(open(intent_file, 'r'))
        self.response_dict = json.load(open(response_file, 'r'))
        super(MailRegexConnector, self).__init__()

    def _process(self, message):
        """
        Process the message data, reformating it so that the model will
        understand it.

        """
        if self.state == 0:
            for item in self.intent_list:
                match = re.match(item['pattern'], message)
                print (item['pattern'])
                
                if match:
                    print (match.groups())
                    return (item['intent'], match.groups())
        else:
            if self.state == 1:
                self.subject = message
            elif self.state == 2:
                self.body = message

        return (None, None)

    def _postprocess(self, intent_tuple):
        """
        Read in the processed message data, pass it to the model object, and
        make a prediction. Return the data dictionary with the prediction
        added to it.

        Returns:
        -------
        dict
        """
        # Return the response to the first occurrence of the pattern in user
        # message
        if self.state == 0:
            (intent, entities) = intent_tuple
            print ("Entities- {}".format(entities))

            response_list = self.response_dict.get(intent)
            if response_list:
                response = random.choice(response_list['messages'])
                if entities:
                    response = response.format(*entities)
                    # FIXME -  assuming only 1 entity
                    # we take the first entity to check for email id
                    entity = entities[0]
                    # FIXME
                    # checking entity by '@' , ideally the connector should have list of 
                    # entities and their types
                    if '@' in entity:
                        self.recipient = entity
                        self.state = 1
            else:
                response = "Could not figure out a proper response. Please try again."
        else:
            if self.state == 1:
                response = "Subject entered - {}. Can you now provide the body?".format(self.subject)
                self.state = 2

            elif self.state == 2:
                response = "Following are the details by you - \n Subtect - {} \n Body {} \n . \
                Please confirm".format(self.subject, self.body)
                self.state = 3

            elif self.state == 3:
                self.state = 0
                send_mail(self.recipient, self.subject, self.body)
                response = "your mail has been sent"
            else:
                self.state = 0
                response = "Could not figure out a proper response. Please try again."

            # save the message somewhere

        return response
