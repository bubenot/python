import telebot
from telebot import types

name = 'WEALYControl | Control Home Server`s'
print("[*] Бот Telegram " + name + " успешно запущен!")

bot = telebot.TeleBot('token')


@bot.message_handler(content_types=['text'])
def main_handler(data):
	print("[->] " + "Получено новое сообщение от пользователя с ID: " + str(int(data.from_user.id)) + " Сообщение: " + str(data.text.lower()))

	if data.from_user.id == 793492772:

		if data.text.lower() == '/start':
			bot.send_message(data.from_user.id, 'Приветствую!!')
	else:
		bot.send_message(data.from_user.id, 'Вы не мой создатель!, и я не могу выполнять Ваши команды!')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(data):
	print("Получено новое событие!")
	#if data.data == 'schedule':
	#	print("[<-] Отправляю расписание на сегодня пользователю с ID: " + str(data.from_user.id))
bot.polling(none_stop=True, interval=0)
