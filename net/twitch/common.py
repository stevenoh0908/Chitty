# net.twitch.common
# common library for getting chat & stream information from Twitch

import requests
import urllib.parse as urlparse

# constants
WS_CHAT_URL = "ws://irc-ws.chat.twitch.tv"
WS_CHAT_ADDEND = "?popout="

RETTYPE_JSON = 0
RETTYPE_TEXT = 1

# methods

def urljoin(baseurl, addurl):
	return f"{baseurl.rstrip('/')}/{addurl}"

def getWebsocketUrl(channel_id):
	baseurl = urljoin(WS_CHAT_URL, channel_id)
	url = urljoin(baseurl, WS_CHAT_ADDEND)
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
