"""
This file is intended for testing purposes only
"""
from state_machine import StateMachine
import json

def test_state_machine():

	# 
	# test 1 -- START to ROOT (should be automatic on creating the statemachine)
	usrQuery = ""
	token_dict = {"entities":[], "intent":""}
	sm = StateMachine()
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))

	#test 2	-- ROOT to RECIPIENT
	usrQuery = "mail to abc@xyz.com"
	token_dict['intent'] = "mail"
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))

	#test 3	-- WRONG VALUE !
	usrQuery = "abc@xyz.com"
	token_dict['intent'] = ""
	token_dict['entities'] = ["", "", "abc@xyz.com"]
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))


	#test 3	-- RECIPIENT to SUBJECT
	usrQuery = "abc@xyz.com"
	token_dict['intent'] = ""
	token_dict['entities'] = ["", "mailid", "abc@xyz.com"]
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))

	#test 4 -- SUBJECT to BODY
	usrQuery = "test"
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))

	#test 5 -- BODY to CONFIRM
	usrQuery = "test"
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))

	#test 6 -- CONFIRM to SEND
	usrQuery = "no"
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))
	#test 7 -- SEND to ROOT (should be automatic after sending mail)
	usrQuery = ""
	print (sm.handleTokens(usrQuery, json.dumps(token_dict)))


if __name__ == "__main__":
	test_state_machine()
