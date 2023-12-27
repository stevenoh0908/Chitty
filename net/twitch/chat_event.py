# net.twitch.chat_event
# common library for getting chat & stream information from Twitch
# chat_event.py

import json

class ChatEvent:
	message = None
	username = None
	userId = None
	badges = None # this will be used for displaying twith badges

	def __init__(self, userId=None, username=None, message=None, badges=None):
		self.message = message
		self.username = username
		self.userId = userId
		self.badges = badges
		pass

	def getMessage(self):
		return self.message

	def getUsername(self):
		return self.username

	def getUserID(self):
		return self.userId

	def getBadges(self):
		return self.badges

	def setMessage(self, message):
		self.message = message

	def setUsername(self, username):
		self.username = username

	def setUserID(self, userId):
		self.userId = userId

	def setBadges(self, badges):
		self.badges = badges

# parse functions

def parseChatEvent(resp):
	elements = resp.split(';')
	for element in elements:
		if 'badges' in element:
			badges = element.lstrip('badges=').split(',')
			pass
		if 'display-name' in element:
			username = element.lstrip('display-name=')
			pass
		if 'user-id' in element:
			userId = element.lstrip('user-id=')
			pass
	message = elements[-1].split(':')[-1].strip()
	return ChatEvent(message=message, userId=userId, username=username, badges=badges)
