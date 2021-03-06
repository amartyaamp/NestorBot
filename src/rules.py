"""
Consists of the rule dictionary to control state transition
Rule intdexed by state name and contains values 
destination state, action and response message.

Keeping in a separate file as rules may get complicated in future
"""

send_mail_transitions = {
  "START": {
    "triggerType": "any",
    "triggerValue": [
      "any"
    ],
    "dest": "ROOT",
    "msg": "Hi! My name is Nestor! I will take care of your mails.",
    "action": "none"
  },
  "ROOT": {
    "triggerType": "intent",
    "triggerValue": [
      "sendmail"
    ],
    "dest": "RCPT",
    "msg": "Sure whom do you wanna mail ?",
    "action": "none"
  },
  "RCPT": {
    "triggerType": "entity",
    "triggerValue": [
      "mailid"          # mailid is a type, so the NLP engine should give us entity type with entity value
    ],
    "dest": "SUBJ",
    "msg": "Mailing to {}. Please enter subject.",
    "action": "store_mailid"
  },
  "SUBJ": {
    "triggerType": "any",
    "triggerValue": [
      "any"
    ],
    "dest": "BODY",
    "msg": "Ok got that! What do you want to say?",
    "action": "store_subj"
  },
  "BODY": {
    "triggerType": "any",
    "triggerValue": [
      "any"
    ],
    "dest": "CNFM",
    "msg": "OK all set! Do you wish to continue?",
    "action": "store_body"
  },
  "CNFM": {
    "triggerType": "msg",
    "triggerValue": [
      "yes",
      "no"
    ],
    "dest": "SENT", #FIXME - might not goto SENT always - couple dest with triggervalue
    "msg": "Sending your mail",
    "action": "send_mail"
  },
  "SENT": {
    "triggerType": "any",
    "triggerValue": [
      "any"
    ],
    "dest": "START",
    "msg": "Your mail has been sent",
    "action": "wait_20"
  }
}