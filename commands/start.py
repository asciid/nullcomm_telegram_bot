from pyrogram import Client, Filters
from commands.tools import get_data
import json

@Client.on_message(Filters.command('start') | Filters.regex('^/start@nullcomm_bot$'))
def start(client, message):
	data = get_data(message)
	name = data['user']['f_name']

	msg = """Привет, {0}. Я - Нуль-тян, но ты можешь называть меня Аней.
Я из nullcomm, и в этом чате я внимательно вас слушаю.
**Основные команды:**
`/start` - Вывести это сообщение;
`/alarm *необяз. аргумент*` - Уведомить всех участников;
`/feedback *сообщение*` - Связаться с моим разработчиков;
`/luv` - Любовь и обнимашки
**А также ролевые:**
`/do *действие*`
`/me *действие*`
`/try *действие*`
Надеюсь, мы хорошо проведём время.""".format(name)
	message.reply(msg)