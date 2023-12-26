# net.chzzk.common
# common library for getting chat & stream information from Naver Chzzk

import requests
import urllib.parse as urlparse

# constants
API_STATUS_URL = "https://api.chzzk.naver.com/polling/v1/channels"
API_CHAT_URL = "https://comm-api.game.naver.com/nng_main/v1/chats"

API_TYPE_STATUS = 0
API_TYPE_CHAT = 1

RETTYPE_JSON = 0
RETTYPE_TEXT = 1

# methods

def urljoin(baseurl, addurl):
	return f"{baseurl.rstrip('/')}/{addurl}"

def getAPIUrl(channel_id, addend, api_type=API_TYPE_STATUS):
	if api_type == API_STATUS_URL:
		baseurl = urljoin(API_STATUS_URL, channel_id)
	else:
		baseurl = API_CHAT_URL
	url = urljoin(baseurl, addend)
	return url

def addParams(url, paramDict):
	url_parse = urlparse.urlparse(url)
	query = url_parse.query
	url_dict = dict(urlparse.parse_qsl(query))
	url_dict.update(paramDict)
	query = urlparse.urlencode(url_dict)
	url_parse = url_parse._replace(query=query)
	return urlparse.urlunparse(url_parse)

def get(url, rettype=RETTYPE_JSON):
	resp = requests.get(url)
	return resp.json() if (rettype == RETTYPE_JSON) else resp.text

def getJsonContent(url):
	jsonObj = get(url, rettype=RETTYPE_JSON)
	return jsonObj['content']

def getJsonContentField(url, field):
	jsonContent = getJsonContent(url)
	return jsonContent[field]
