# net.chzzk.chat
# library for getting chat & stream information from Naver Chzzk
# chat

from net.chzzk.common import *
import net.chzzk.chat_event as chat_event
import asyncio, websockets, json

# constants
WS_CHAT_URL = "wss://kr-ss1.chat.naver.com/chat"

# async methods
async def listen(chat_channel_id, access_token, max_retry=5):
	async with websockets.connect(WS_CHAT_URL) as socket:
		# send first-connection json req
		tryCount = 0
		sid = None
		while True:
			jsonObj = json.dumps({
				"ver": "2", "cmd": 100, "svcid": "game", "tid": 1,
				"cid": chat_channel_id,
				"bdy": {
					"uid": None,
					"devType": 2001,
					"auth": "READ",
					"accTkn": access_token
				}
			})
			await socket.send(jsonObj)
			resp = await socket.recv()
			# check whether first-connection is successful
			jsonObj = json.loads(resp)
			if jsonObj['retMsg'] == 'SUCCESS':
				sid = jsonObj['bdy']['sid']
				break
			elif tryCount > max_retry:
				raise Exception('Chat Server Connection Failed')
				pass
			tryCount += 1
			pass
		# send Second-connection json req, after that, always recv
		jsonObj = json.dumps({
			"ver": "2", "cmd": 5101, "svcid": "game", "tid": 2,
			"cid": chat_channel_id,
			"bdy": {"recentMessageCount": 50} 
		})
		await socket.send(jsonObj)
		# after this, the chat server will send recent messages
		resp = await socket.recv()
		jsonObj = json.loads(resp)
		# parse chat event here at first (this will be recent messages)
		# for testing in cmd (27 Dec 2023 03:48)
		recent_chats = chat_event.parseChatEvents(jsonObj)
		for chat in recent_chats:
			print(f'{chat.getUsername()}: {chat.getMessage()}')
			pass
		while True:
			resp = await socket.recv()
			jsonObj = json.loads(resp)
			# if resp is alive-check, respond it.
			if jsonObj['cmd'] == 0:
				jsonObj = json.dumps({
					"ver": "2", "cmd": 10000
				})
				await socket.send(jsonObj)
				pass
			else: # this must be chat event
				# parse chat event here
				# for testing in cmd (27 Dec 2023 03:48)
				chat = chat_event.parseChatEvent(jsonObj)
				print(f'{chat.getUsername()}: {chat.getMessage()}')
				pass
			pass
		pass
	pass

# methods
def getField(chat_channel_id, field):
	url = getAPIUrl(chat_channel_id, ADDEND_ACCESS_TOKEN, api_type=API_TYPE_CHAT)
	url = addParam(url, {'channelId': str(chat_channel_id), 'chatType': 'STREAMING'})
	return getJsonContentField(url, field)

def getAccessToken(chat_channel_id):
	return getField(chat_channel_id, 'accessToken')

def getExtraToken(chat_channel_id):
	return getField(chat_channel_id, 'extraToken')
