import telebot
from decouple import config

token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgQAAxkBAAEIBXpkBYbdskuTAAHrhE_wnDdcsOeaQcIAAhsDAALZI2Qh3SOl9rFb6KUuBA'
no_sticker = 'CAACAgQAAxkBAAEIBZFkBYc2OKQpCiZs7sMyi4-8c86BhgACQAMAAtkjZCEpgu9UAo73eC4E'

# клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1, b2)


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выбери кнопку', reply_markup=keyboard)

# func - функция фильтр, в данном случае разрешаются все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)


bot.polling()

