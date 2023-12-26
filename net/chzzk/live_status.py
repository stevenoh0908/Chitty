# net.chzzk.live_status
# library for getting chat & stream information from Naver Chzzk
# live-status parser

from net.chzzk.common import *

# constants
ADDEND_LIVE_STATUS = 'live-status'

# methods
def getField(channel_id, field):
	url = getAPIUrl(channel_id, ADDEND_LIVE_STATUS, api_type=API_TYPE_STATUS)
	return getJsonContentField(url, field)

def getLiveTitle(channel_id):
	return getField(channel_id, 'liveTitle')

def getStatus(channel_id):
	return getField(channel_id, 'status')

def getConcurrentUserCount(channel_id):
	return getField(channel_id, 'concurrentUserCount')

def getAccumulateCount(channel_id):
	return getField(channel_id, 'accumulateCount')

def getPaidPromotion(channel_id):
	return getField(channel_id, 'paidPromotion')

def getAdult(channel_id):
	return getField(channel_id, 'adult')

def getChatChannelId(channel_id):
	return getField(channel_id, 'chatChannelId')

def getCategoryType(channel_id):
	return getField(channel_id, 'categoryType')

def getLiveCategory(channel_id):
	return getField(channel_id, 'liveCategory')

def getLiveCategoryValue(channel_id):
	return getField(channel_id, 'liveCategoryValue')
