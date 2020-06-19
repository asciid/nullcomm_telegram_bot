from pyrogram import Client, Filters
from commands.tools import get_data, check_command
import random
import json

@Client.on_message(Filters.regex('^/do') | Filters.regex('^/do@nullcomm_bot'))
def role_do(client, message):

	data = get_data(message)
	name = data['user']['f_name']

	argument = check_command(message, '/do', True)
	
	if argument != 'err':
		message.reply("[**{0}**] __({1})__".format(argument, name))

@Client.on_message(Filters.regex("^/me") | Filters.regex('^/me@nullcomm_bot'))
def role_me(client, message):

	data = get_data(message)
	name = data['user']['f_name']

	argument = check_command(message, '/me', True)

	if argument != 'err':
		message.reply("***{0}** {1}".format(name, argument))

@Client.on_message(Filters.regex('/try') | Filters.regex('/try@nullcomm_bot'))
def role_try(client, message):
	
	data = get_data(message)
	name = data['user']['f_name']
	
	random.seed()
	
	if random.randint(0,1): state = 'УСПЕХ'
	else: state = 'ПРОВАЛ'

	argument = check_command(message, '/try', True)

	if argument != 'err':
		message.reply("***{0}** {1} **[{2}]**".format(name, argument, state))