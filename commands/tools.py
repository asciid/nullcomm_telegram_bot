from pyrogram import Client, Filters
import json

admin_uid = 298686852
nullcomm_gid = -1001292559576

# "Long" commands (usually in groups and with Botfather's command list) look like:
# /command@bot_nickname
bot_nickname = "@nullcomm_bot"

def get_data(message):
	raw = json.loads(str(message))

	UID = raw['from_user']['id']
	GID = raw['chat']['id']
	msg = raw['text']
	first_name = raw['from_user']['first_name']
	#data = {'UID': UID, 'GID': GID, 'msg': msg, 'first_name': first_name}

	#return data
	return UID, GID, msg, first_name

def check_command(message, command, delete):

	UID, GID, msg, first_name = get_data(message)
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
		else: return argument
