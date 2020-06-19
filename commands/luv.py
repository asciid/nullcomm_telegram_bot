from pyrogram import Client, Filters
from commands.tools import get_data
from random import randint
import json

@Client.on_message(Filters.regex('^/luv$') | Filters.regex('^/luv@nullcomm_bot$'))
def luv(client, message):

	data = get_data(message)
	UID, GID = data['user']['id'], data['group']['id']
	name = data['user']['f_name']

	phrases = [
	'Ну не сегодня.',
	'{0}, ты чего? Люди же смотрят!'.format(name),
	'Я занята, давай потом...',
	'Я не в настроении.',
	'Не приставай, хватит.',
	'Да как ты смеешь?',
	'Я админа позову!',
	'Ты странный какой-то.',
	'Хотелка не выросла',
	'**[эти дни]**'
	]

	print(message)

	if UID == GID:
		message.reply('~ И я люблю тебя, {0} <3 ~'.format(name), UID)
	else:
		message.reply(phrases[randint(0, len(phrases) - 1)])