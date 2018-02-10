"""
This file is intended for testing purposes only
"""
from state_machine import StateMachine
import json

def test_state_machine():

	usrQuery = ""
	token_dict = json.dumps({"entities":[], "intent":""})
	sm = StateMachine()

	print (sm.handleTokens(usrQuery, token_dict))

if __name__ == "__main__":
	test_state_machine()
