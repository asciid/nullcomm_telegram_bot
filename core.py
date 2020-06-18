#!/usr/bin/env python3

"""
	Behold! null-tan!

	   GENERAL NOTES:

	1. I use Filters.regex() instead of .commands(). 
	   The second can't handle spaces between a command and an argument.

	2. I put some commands in the main file as some functions
	   need to use Client's object and it can't be declared twice. 

	3. comamnds.tools module was made to don't repeat lotta times
	   I need to get UID/GID and other data from message's JSON.
	   It's a pity library has no method to get data without pasring.
	
	   TODO:

	* /getme: info about sender

		DONE:

	* /start
	* /feedback *message*
	* /alarm    *message* (optional)

	* /try      *action*
	* /me       *action*
	* /do       *action*
"""

from pyrogram import Client, Filters
from commands.tools import get_data, admin_uid, check_command
import os.path
import json

if os.path.exists('bot.ini'):
	app = Client("nullcomm", config_file="bot.ini")
else:
	print('Осутствует конфигурационный файл bot.ini!')
	exit()

#  ----------
# | Commands |
#  ----------

@app.on_message(Filters.regex('^/alarm') | Filters.regex('^/alarm@nullcomm_bot'))
def alarm(client, message):

	UID, GID, msg, name = get_data(message)
	reply = ""

	# /alarm smthn
	#        ^ <-- 7
	# /alarm@nullcomm_bot smthn
	#                     ^ <-- 20

	if UID != admin_uid:
		message.reply('Увы, вы не имеете достаточно прав для массового оповещения.\nИли, возможно, хулиганите ;)\n*грозит пальцем*')
	else:

		if msg == '/alarm' or msg == '/alarm@nullcomm_bot':
			reply = "**АЛЯРМА! МАССОВОЕ СОБРАНИЕ!**\n"

		else:
			if msg.startswith('/alarm@nullcomm_bot'):
				alert = msg[20:]
			else:
				alert = msg[7:]

			if alert[-1] != "!":
				alert += "!"
		
			reply = "**АЛЯРМА! {}**\n".format(alert)
		
		for member in app.iter_chat_members(GID):
			if not member.user.is_bot:
				reply += "[{}](tg://user?id={}), ".format(member.user.first_name, member.user.id)
		
		reply = reply[:len(reply)-2]

		message.reply(text=reply, reply_to_message_id=UID, parse_mode='markdown')

@app.on_message(Filters.regex('^/feedback') | Filters.regex('^/feedback@nullcomm_bot'))
def feedback(client, message):
	
	UID, GID, msg, name = get_data(message)
	argument = check_command(message, '/feedback', False)

	if argument != 'err':
		app.send_message(admin_uid, "**Обратная связь:**\n[{0}](tg://user?id={1}): {2}".format(name, UID, argument))
		message.reply('Ваше сообщение успешно передано!', UID)

app.run()