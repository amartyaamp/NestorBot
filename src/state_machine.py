"""
The StateMachine Class.
It consists of a state and a transition rules dictionary for different state
"""
import rules
import json


class StateMachine:

	def __init__(self):

		self.state = "START"
		self.rulesDict = rules.send_mail_transitions
		## TODO - self.context to store the user context

	
	def handleTokens(self, usrQuery, tokens):

		print(usrQuery)

		token_dict = json.loads(tokens)
		token_dict["msg"] = usrQuery
		print("token_dict to changeState - {}".format(token_dict["msg"]))
		## change state
		action, response = self.changeState(token_dict)

		return action, response

 
	def changeState(self, token_dict):
		# change the state if trigger is fired 

		action, response = "none", "do you know english?? enter stop or \
		abort to start again"
		
		#ensure the trigger has been fired
		# if abort or stop in msg then goto start

		if "abort" in token_dict["msg"]:
			print ("got abort from usrQuery. Going to start")
			self.state = "START"
			response = "aborting ..."
		elif self.triggerFired(token_dict['msg'],
			token_dict['intent'], token_dict['entities']):
			
			#change the state
			print ("changing the state now")
			
			action = self.rulesDict[self.state]["action"]
			response = self.rulesDict[self.state]["msg"]
			self.state = self.rulesDict[self.state]["dest"]
			print ("state changed to - {}".format(self.state))
			
		return action, response


	def triggerFired(self, msg, intent, entities):

		res = False;

		#check the trigger type for current state
		triggerType = self.rulesDict[self.state]['triggerType']
		trigerValues = self.rulesDict[self.state]['triggerValue']
		
		if triggerType == "any":
			res = True
			return res

		for tv in triggerValues:
		
			# if intent look in intent
			if triggerType == "intent":
				if tv in intent :
					res = True
					break

			# same for msg, entity
			if triggerType == "msg":
				if tv in msg :
					res = True
					break

			if triggerType == "entity":
				if tv in entities:
					res = True
					break
		#end for

		return res;
		