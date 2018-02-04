"""
The StateMachine Class.
It consists of a state and a transition rules dictionary for different state
"""
class StateMachine:

	def __init__(self):

		self.state = State()
		self.rulesDict = {}


	def handleTokens(tokens):

		token_dict = json.load(tokens)
		action, reponse = changeState(token_dict)

		return botResponse

	