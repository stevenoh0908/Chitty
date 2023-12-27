# net.twitch.chat
# library for getting chat & stream information from Twitch
# chat

from net.twitch.common import *
import net.twitch.chat_event as chat_event
import asyncio, websockets

# contstants

# async methods
async def listen(chat_channel_id, nickname, max_retry=5):
	async with websockets.connect(WS_CHAT_URL) as socket:
		# send first-connection reqs
		tryCount = 0
		while True:
			await socket.send("CAP REQ :twitch.tv/tags twitch.tv/commands")
			await socket.send("PASS SCHMOOPIIE")
			await socket.send(f"NICK {nickname}")
			await socket.send(f"USER {nickname} 8 * :{nickname}")
			# check whether first-connection is successful
			resp = await socket.recv()
			resp = await socket.recv()
			if 'Welcome' in resp:
				break
			tryCount += 1
			pass
		# send channel name to join chat room
		await socket.send(f"""JOIN #{chat_channel_id}""")
		# get room join resp
		resp = await socket.recv()
		if 'JOIN' not in resp:
			raise Exception("Something wrong with Joining Twitch Chat Room")
			return
		resp = await socket.recv()
		# from now on, the chat server will convey chat events and ping-pong events
		while True:
			resp = await socket.recv()
			# if it is a ping-pong check, respond to it.
			if 'PING' in resp:
				await socket.send('PONG')
				pass
			else:
				# for debugging
				chat = chat_event.parseChatEvent(resp)
				print(f"{chat.getUsername()}: {chat.getMessage()}")
				# parse messages
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
