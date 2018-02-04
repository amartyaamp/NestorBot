"""
The StateMachine Class.
It consists of a state and a transition rules dictionary for different state
"""
import rules

class StateMachine:

	def __init__(self):

		self.state = "START"
		self.rulesDict = rules.send_mail_transitions
		## TODO - self.context to store the user context


	def handleTokens(self, usrQuery, tokens):

		token_dict = json.load(tokens)
		token_dict["msg"] = usrQuery
		## change state
		action, reponse = changeState(token_dict)

		return action, response

	def changeState(self, token_dict):
		# change the state if trigger is fired 

		action = "none", response = "do you know english?? enter stop or \
		abort to start again"
		
		#ensure the trigger has been fired
		# if abort or stop in msg then goto start

		if "abort" in token_dict["msg"]:
			self.state = "START"
			response = "aborting ..."
		elif triggerFired(token_dict['msg'],
			token_dict['intent'], token_dict['entities']):
			
			#change the state
			self.state = self.rulesDict[self.state]["dest"]
			action = self.rulesDict[self.state]["action"]
			response = self.rulesDict[self.state]["action"]
		else:
			# there is an unknown input, dont need to do anything as 
			# action and response are already set to default

		return action, response
	
	def triggerFired(self, msg, intent, entities):

		res = False;

		#check the trigger type for current state
		triggerType = self.rulesDict[self.state]['triggerType']
		trigerValues = self.rulesDict[self.state]['triggerVal']

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
		