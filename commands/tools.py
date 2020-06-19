from pyrogram import Client, Filters
import json

admin_uid = 298686852
nullcomm_gid = -1001292559576
bot_nickname = "@nullcomm_bot"

# "Long" commands (usually in groups and with Botfather's command list) look like:
# /command@bot_nickname

def get_data(message):
	raw = json.loads(str(message))

	try: l_name = raw['from_user']['last_name']
	except KeyError: l_name = ''

	try: username = raw['from_user']['username']
	except KeyError: username = ''

	try: lang = raw['from_user']['language_code']
	except KeyError: lang = ''

	data = {
		'user': {
			'id': raw['from_user']['id'],
			'f_name': raw['from_user']['first_name'],
			'l_name': l_name,
			'restricted': raw['from_user']['is_restricted'],
			'verified': raw['from_user']['is_verified'],
			'scam': raw['from_user']['is_scam'],
			'status': raw['from_user']['status'],
			'username': username,
			'lang': lang
		},
		'group': {
			'id': raw['chat']['id'],
			'restricted': raw['chat']['is_restricted'],
			'verified': raw['chat']['is_verified'],
			'scam': raw['chat']['is_scam']
		},
		'message': raw['text']
	}

	return data

def check_command(message, command, delete):

	data = get_data(message)
	msg = data['message']
	err = False

	# Handle empty argument
	if msg == command or msg == command + bot_nickname:
		message.reply('Увы, команда `{0}` имеет обязательный аргумент:\n`{0} аргумент`'.format(command))
		err = True

	## Get argument's position
	# /test argument
	#       ^ <-- 6 <-- len('/test') + 1 (space)
	# /test@nullcomm_bot argument
	# 

	if msg.startswith(command + ' '): argument = msg[(len(command) + 1):]
	elif msg.startswith(command + bot_nickname + ' '): argument = msg[(len(command) + len(bot_nickname) + 1):]
	else: err = True

	if err: return 'err'
	else: 
		if delete: message.delete()
		return argument
