from pyrogram import Client, Filters
import json

@Client.on_message(Filters.regex('^/getme$') | Filters.regex('^/getme@nullcomm_bot$'))
def getme(client, message):
	data  = json.loads(str(message))
	
	UID        = data['from_user']['id']
	scam       = data['from_user']['is_scam']
	verified   = data['from_user']['is_verified']
	restricted = data['from_user']['is_restricted']

	message.reply(
"""
Ваш ID: `{0}`
Помечен как мошенник: `{1}`
Подтверждён: `{2}`
Ограничен: `{3}`
Допишите меня кто-нибудь...
""".format(UID, scam, verified, restricted), UID)