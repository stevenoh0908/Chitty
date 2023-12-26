# net.chzzk.chat_access_token
# library for getting chat & stream information from Naver Chzzk
# chat access token

from net.chzzk.common import *

# constants
ADDEND_ACCESS_TOKEN = 'access-token?'

# methods
def getField(chat_channel_id, field):
	url = getAPIUrl(chat_channel_id, ADDEND_ACCESS_TOKEN, api_type=API_TYPE_CHAT)
	url = addParams(url, {'channelId': str(chat_channel_id), 'chatType': 'STREAMING'})
	return getJsonContentField(url, field)

def getAccessToken(chat_channel_id):
	return getField(chat_channel_id, 'accessToken')

def getExtraToken(chat_channel_id):
	return getField(chat_channel_id, 'extraToken')
