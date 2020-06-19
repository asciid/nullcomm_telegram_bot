from pyrogram import Client, Filters
from commands.tools import get_data
import json

@Client.on_message(Filters.regex('^/getme$') | Filters.regex('^/getme@nullcomm_bot$'))
def getme(client, message):
	data = get_data(message)
	user = data['user']

	message.reply(
"""
**{0} {1}**
**Короткое имя**: @{2}
**UID**: {3};
**Статус**: {4}
**Язык**: {5};
**Помечен как мошенник**: {6};
**Ограничен**: {7};
**Подтверждён**: {8};
**Ссылка**: [{0}](tg://user?id={3})""".format(user['f_name'], user['l_name'], user['username'], user['id'], user['status'], user['lang'], user['scam'], user['restricted'], user['verified']))