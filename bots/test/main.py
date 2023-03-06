import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    # bot.send_message('892891195', 'Hello')
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEIBTNkBXYgGq10XERrV25pLiLFrhxi3AAC9AIAAtkjZCGmdye4daM15C4E')
    bot.send_photo(message.chat.id, 'https://www.planetware.com/wpimages/2019/11/canada-in-pictures-beautiful-places-to-photograph-morraine-lake.jpg')

@bot.message_handler(content_types=['text'])
def aaaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщенрие не распознано')

@bot.message_handler(content_types=['sticker'])
def bbbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()



