"""
Takes responsibility of all attachment creation for messages
Used mostly for adaptive cards implementation.


"""
from botbuilder.schema import (Attachment)

class AdaptiveCard(Attachment):
    """
    Adaptive card is just an attachment with adaptive card contentType
    We just choose the body and actions
    """

    def __init__(self, content=None):
        super(AdaptiveCard, self).__init__()
        self.content_type = "application/vnd.microsoft.card.adaptive"
        
        # either set the content param or get a default content
        self.content = content
        if not content:
            self.content = self.__get_content()

    def __get_content(self):

        # Inits a default body and content

        # create the actions
        actions = [ {
            "type": "Action.OpenUrl",
            "url": "http://adaptivecards.io",
            "title": "Learn More"
          }]

        body =[{
            "type": "TextBlock",
            "text": "Hi I am Nestor!!",
            "size": "large"
          },
          {
            "type": "TextBlock",
            "text": "Let me handle your mails ..."
          },
        ]

        content = dict(type="AdaptiveCard", version="1.0", body=body, actions=actions)

        return content


def get_attachments():
    
    print("[attachmentsLog] creating adaptive card attachment")
    attch = AdaptiveCard()
    return [attch]    