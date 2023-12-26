# net.chzzk.common
# common library for getting chat & stream information from Naver Chzzk
# chat_event.py

import json

class ChatEvent:
	message = None
	username = None
	userId = None # this will be used for calculating user-displaying color

	def __init__(self, userId=None, username=None, message=None):
		self.message = message
		self.username = username
		self.userId = userId
		pass

	def getMessage(self):
		return self.message

	def getUsername(self):
		return self.username

	def getUserID(self):
		return self.userId

	def setMessage(self, message):
		self.message = message

	def setUsername(self, username):
		self.username = username

	def setUserID(self, userId):
		self.userId = userId

# parse functions

def parseChatEventBody(bodyJsonObj):
	profileJsonObj = json.loads(bodyJsonObj['profile'])
	if 'msg' in bodyJsonObj:
		message = bodyJsonObj['msg']
		pass
	else:
		message = bodyJsonObj['content']
		pass
	if 'uid' in bodyJsonObj:
		userId = bodyJsonObj['uid']
		pass
	else:
		userId = bodyJsonObj['userId']
		pass
	return ChatEvent(message=message, userId=userId, username=profileJsonObj['nickname'])

def parseChatEvent(respJsonObj):
	return parseChatEventBody(respJsonObj['bdy'][0])

def parseChatEvents(respJsonObj):
	chatevents = []
	for bodyJsonObj in respJsonObj['bdy']['messageList']:
		chatevents.append(parseChatEventBody(bodyJsonObj))
		pass
	return chatevents
