import telebot
import requests
import time

# t.me/fillomaniya_bot
bot = telebot.TeleBot("5880836899:AAFgP0X_f5Y-5BaRGfA0ityMWMeBo96rz1E", parse_mode=None)

@bot.message_handler(content_types=['text'])
def hello_user(message):
    if 'привет' in message.text:
        bot.reply_to(message, 'привет ' + message.from_user.first_name)
    elif message.text == 'играть':
        bot.reply_to(message, 'хочешь поиграть?')
    elif message.text == 'погода':
        r = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, r.text)
    elif message.text == 'котик':
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text == 'файл':
        doc = open('python/seminar_9/file.txt')
        bot.send_document(message.chat.id, doc)
        doc.close()

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()