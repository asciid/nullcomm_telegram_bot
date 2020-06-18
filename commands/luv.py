from pyrogram import Client, Filters
import json
from commands.tools import get_data

@Client.on_message(Filters.regex('^/luv$') | Filters.regex('^/luv@nullcomm_bot$'))
def luv(client, message):
	data = json.loads(str(message))

	UID = data['from_user']['id']
	GID = data['chat']['id']
	name = data['from_user']['first_name']

	get_data(message)

	if UID == GID:
		message.reply("~ И я люблю тебя, {0} <3 ~".format(name), UID)
	else:
		message.reply('Я не такая! Какого ты обо мне мнения?!')
