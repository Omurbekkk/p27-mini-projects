import telebot
from decouple import config

token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgQAAxkBAAEIBXpkBYbdskuTAAHrhE_wnDdcsOeaQcIAAhsDAALZI2Qh3SOl9rFb6KUuBA'
no_sticker = 'CAACAgQAAxkBAAEIBZFkBYc2OKQpCiZs7sMyi4-8c86BhgACQAMAAtkjZCEpgu9UAo73eC4E'

bot = telebot.TeleBot(token)

# клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('Да')
b2 = telebot.types.KeyboardButton('Нет')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')
    
    bot.register_next_step_handler(message, reply_to_button)

bot.polling()



