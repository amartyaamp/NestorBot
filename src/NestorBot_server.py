# 
import http.server
import json
from botbuilder.schema import (Activity, ActivityTypes)
from botbuilder.core import BotFrameworkAdapter

# import Components
from luis_setter import LuisBotSetter
from state_machine import StateMachine
from actions import Actions
from attachments import get_attachments


#Debugging only
import pdb

# APP_ID and APP_PASSWORD for 
APP_ID = ''
APP_PASSWORD = ''

# Init components - this is out of requesthandler because 1 instance of request handler is created every request
# NLP engine
_nlp = LuisBotSetter()
#state machine
_sm = StateMachine()
#action handler
_action_hnd = Actions()

# RequestHandler  is the service component that a channel connects to

class BotRequestHandler(http.server.BaseHTTPRequestHandler):

	# create the activity object to send to channel
	@staticmethod
	def __create_reply_activity(request_activity, text, attachments=None):
		reply_activity = Activity(
			type=ActivityTypes.message,
			channel_id=request_activity.channel_id,
			conversation=request_activity.conversation,
			recipient=request_activity.from_property,
			from_property=request_activity.recipient,
			text=text,
			service_url=request_activity.service_url,
			attachments=attachments)

		return reply_activity

	# conversationUpdate message marks on start of a conversation. REST response status code - 202
	def __handle_conversation_update_activity(self, activity: Activity):
		self.send_response(202)
		self.end_headers()
		if activity.members_added[0].id != activity.recipient.id:
			#change the state to ROOT
			action, response, _ = _sm.handleTokens("", json.dumps({"entity":[], "intent":""}))
			# perform some action - although nothing happens in actual here!
			_action_hnd.perform_action(action, activity.text)
			attachments = get_attachments()
			self._adapter.send([BotRequestHandler.__create_reply_activity(activity, response, attachments)])

	# inConversation messages -  within a conversation. REST response status code - 200
	def __handle_message_activity(self, activity: Activity):
		self.send_response(200)
		self.end_headers()
		# get the entities, intent from NLP engine - LUISBot for now
		tokens = _nlp.getTokens(activity.text)
		print ("[log] - got tokens - {}".format(tokens))

		runLoop, firstPass = False, True
		usrQuery = activity.text
		while runLoop or firstPass:
			firstPass = False # we don't have do-while in python :(

			# change state
			action, response, runLoop = _sm.handleTokens(usrQuery, tokens)

			# by action code, do a background processing
			_action_hnd.perform_action(action, usrQuery)
			# send the message to channel
			self._adapter.send([BotRequestHandler.__create_reply_activity(activity, response)])
			#reset the usrQuery
			usrQuery = ""



	# messages not understood by the bot
	def __unhandled_activity(self):
		self.send_response(404)
		self.end_headers()

	# point of conversation loop. inputs -  activity from channel,  output - activity to channel
	def on_receive(self, activity: Activity):
		if activity.type == ActivityTypes.conversation_update.value:
			self.__handle_conversation_update_activity(activity)
		elif activity.type == ActivityTypes.message.value:
			self.__handle_message_activity(activity)
		else:
			self.__unhandled_activity()

	# parse the POST message from channel
	def do_POST(self):

		body = self.rfile.read(int(self.headers['Content-Length']))
		
		# get data into json
		data = json.loads(str(body, 'utf-8'))
		print ("POST data - {}".format(data))

		activity = Activity.deserialize(data)
		print ("Activity data - {}".format(activity))
		self._adapter = BotFrameworkAdapter(APP_ID, APP_PASSWORD)
		self._adapter.on_receive = self.on_receive
		self._adapter.receive(self.headers.get("Authorization"), activity)


# Run start the server and keep running
def main():
	try:
		SERVER = http.server.HTTPServer(('localhost', 9000), BotRequestHandler)
		print('Started http server on localhost:9000')
		SERVER.serve_forever()
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		SERVER.socket.close()


if __name__ == "__main__":
	main()