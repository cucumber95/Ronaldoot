import telebot
from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('5871674630:AAF4240GdY2Cvx_2Nnir3gwWlDQJzwdiOTc')

import asyncio
import random
import os

f = open('quotes.txt', 'r', encoding='UTF-8')
quotes = f.read().split('\n')
f.close()

@bot.message_handler(commands=['start'])
async def get_start(message):
	await bot.send_message(message.chat.id, 'Приветствую фаната Cristiano Ronaldo!')

@bot.message_handler(commands=['help'])
async def get_help(message):
	await bot.send_message(message.chat.id, '\\help - отобразить данное сообщение\n\\start - запустить бота\n\\quote - получить случайную великую цитату Роналду\n\\picture - получить случайную фотографию величайшего Роналду\n\\extreme_picture - получить случайную эксклюзивную фотографию величайшего Роналду\n\\get_siuuu - SIUUUUUUU')

@bot.message_handler(commands=['quote'])
async def get_quote_from_Ronaldo(message):
	await bot.send_message(message.chat.id, random.choice(quotes))
	
@bot.message_handler(commands=['picture'])
async def get_picture_of_Ronaldo(message):
	photo = open('pictures/' + random.choice(os.listdir('pictures')), 'rb')
	await bot.send_photo(message.from_user.id, photo, caption = 'Siuuuuuuuu')

@bot.message_handler(commands=['extreme_picture'])
async def get_extreme_picture_of_Ronaldo(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	key_yes = telebot.types.InlineKeyboardButton(text="Да😎", callback_data='yes')
	key_no = telebot.types.InlineKeyboardButton(text="Нет😥", callback_data='no')
	keyboard.add(key_yes)
	keyboard.add(key_no)
	await bot.send_message(message.chat.id, 'Вам уже исполнилось 18 лет?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
async def extreme_picture_of_Ronaldo_callback(call):
	if call.data == "yes":
		photo = open('extreme_pictures/' + random.choice(os.listdir('extreme_pictures')), 'rb')
		await bot.send_photo(call.message.chat.id, photo, caption = 'Muchas gracias afición, esto es para vosotros Siuuu')
	elif call.data == "no":
		await bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEG9oVjpZOPws9EkTQ8Tw4e8UWV92hMYAACnRMAAlUN0Usy7AKRISy9QiwE')
		await bot.send_message(call.message.chat.id, 'Отказано в доступе😩')

@bot.message_handler(commands=['get_siuuu'])
async def get_siuuu(message):
	await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=0acgpCo6HFc')

if __name__ == '__main__':
    asyncio.run(bot.polling(non_stop=True))